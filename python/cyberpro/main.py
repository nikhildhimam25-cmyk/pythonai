# layer1_recon.py
import asyncio
import subprocess
import json
import httpx
import socket
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, asdict
from typing import List, Dict
import requests
from zapv2 import ZAPv2  # pip install python-owasp-zap-v2.4

# ─────────────────────────────────────────
# DATA MODEL
# ─────────────────────────────────────────

@dataclass
class ReconResult:
    target: str
    subdomains: List[str] = field(default_factory=list)
    ips: List[str] = field(default_factory=list)
    open_ports: Dict[str, List[Dict]] = field(default_factory=dict)
    dns_records: Dict[str, List] = field(default_factory=dict)
    live_urls: List[Dict] = field(default_factory=list)
    spidered_urls: List[str] = field(default_factory=list)

# ─────────────────────────────────────────
# AGENT 1 — SUBFINDER (Subdomain Enum)
# ─────────────────────────────────────────

import requests

class SubfinderAgent:
    def run(self, domain: str) -> List[str]:
        results = set()
        results.update(self._crtsh(domain))
        results.update(self._hackertarget(domain))
        results.update(self._threatcrowd(domain))
        results.update(self._alienvault(domain))
        return list(results)

    def _crtsh(self, domain: str) -> List[str]:
        """Certificate transparency logs — most powerful free source"""
        try:
            r = requests.get(
                f"https://crt.sh/?q=%.{domain}&output=json",
                timeout=30
            )
            entries = r.json()
            subs = set()
            for e in entries:
                name = e.get("name_value", "")
                for sub in name.split("\n"):
                    sub = sub.strip().lstrip("*.")
                    if domain in sub:
                        subs.add(sub)
            return list(subs)
        except Exception as e:
            print(f"[crtsh] {e}")
            return []

    def _hackertarget(self, domain: str) -> List[str]:
        try:
            r = requests.get(
                f"https://api.hackertarget.com/hostsearch/?q={domain}",
                timeout=15
            )
            return [line.split(",")[0] for line in r.text.splitlines() if domain in line]
        except:
            return []
        

    def _alienvault(self, domain: str) -> List[str]:
        try:
            r = requests.get(
                f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns",
                timeout=15
            )
            return [e["hostname"] for e in r.json().get("passive_dns", []) if domain in e.get("hostname","")]
        except:
            return []

    def _threatcrowd(self, domain: str) -> List[str]:
        try:
            r = requests.get(
                f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}",
                timeout=15
            )
            return r.json().get("subdomains", [])
        except:
            return []
# ─────────────────────────────────────────
# AGENT 2 — NMAP (Port + Service Scan)
# ─────────────────────────────────────────

class NmapAgent:
    def run(self, targets: List[str]) -> Dict[str, List[Dict]]:
        results = {}
        # Run all hosts in parallel using nmap's own parallelism
        target_str = " ".join(targets[:50])
        
        result = subprocess.run([
            "nmap",
            "-sV",           # service version detection
            "-sC",           # default scripts
            "-T4",           # aggressive timing
            "--open",        # only open ports
            "-p", "1-10000", # top 10k ports (or use --top-ports 1000)
            "--min-rate", "1000",   # packets per second
            "--max-retries", "1",
            "-oX", "-",      # XML to stdout
            *targets[:50]    # nmap handles parallelism internally
        ], capture_output=True, text=True, timeout=300)
        
        return self._parse_xml_multi(result.stdout)
    
    def _parse_xml_multi(self, xml: str) -> Dict:
        import xml.etree.ElementTree as ET
        results = {}
        try:
            root = ET.fromstring(xml)
            for host_el in root.findall("host"):
                addr_el = host_el.find("address")
                if addr_el is None:
                    continue
                ip = addr_el.get("addr", "unknown")
                ports = []
                for port in host_el.findall(".//port"):
                    state = port.find("state")
                    service = port.find("service")
                    if state is not None and state.get("state") == "open":
                        ports.append({
                            "port": int(port.get("portid")),
                            "protocol": port.get("protocol"),
                            "service": service.get("name") if service is not None else "unknown",
                            "version": service.get("version","") if service is not None else ""
                        })
                if ports:
                    results[ip] = ports
        except ET.ParseError as e:
            print(f"[nmap] XML parse error: {e}")
        return results

# ─────────────────────────────────────────
# AGENT 3 — DNSDUMPSTER (DNS Mapping)
# ─────────────────────────────────────────

class DNSDumpsterAgent:
    """Scrapes DNSDumpster for DNS records."""

    BASE = "https://api.hackertarget.com"

    def run(self, domain: str) -> Dict[str, List]:
        print(f"[dnsdumpster] Fetching DNS records for {domain}")
        return {
            "a":     self._query("hostsearch", domain),
            "mx":    self._query("dnslookup", domain, "MX"),
            "ns":    self._query("dnslookup", domain, "NS"),
            "txt":   self._query("dnslookup", domain, "TXT"),
        }

    def _query(self, endpoint: str, domain: str, rtype: str = None) -> List[str]:
        try:
            url = f"{self.BASE}/{endpoint}/?q={domain}"
            if rtype:
                url = f"{self.BASE}/dnslookup/?q={domain}&type={rtype}"
            r = requests.get(url, timeout=15)
            return [line.strip() for line in r.text.split("\n") if line.strip() and "error" not in line.lower()]
        except Exception as e:
            print(f"[dnsdumpster] {e}")
            return []

# ─────────────────────────────────────────
# AGENT 4 — OWASP ZAP (Web Spider)
# ─────────────────────────────────────────

class OWASPZapAgent:
    """Spiders a target using ZAP API (ZAP must be running)."""

    def run(self, urls: List[str]) -> List[str]:
        print(f"[ZAP] Spidering {len(urls)} URLs")
        discovered = []
        try:
            zap = ZAPv2(apikey="changeme", proxies={"http": "http://127.0.0.1:8080"})
            for url in urls[:5]:
                scan_id = zap.spider.scan(url)
                while int(zap.spider.status(scan_id)) < 100:
                    asyncio.sleep(2)
                discovered.extend(zap.spider.results(scan_id))
        except Exception as e:
            print(f"[ZAP] Not available: {e} — skipping spider")
        return list(set(discovered))

# ─────────────────────────────────────────
# AGENT 5 — HTTPX (Live URL Probe)
# ─────────────────────────────────────────

class HttpxAgent:
    """Probes URLs for liveness, status codes, headers, tech stack."""

    def run(self, targets: List[str]) -> List[Dict]:
        print(f"[httpx] Probing {len(targets)} targets")
        results = []
        with ThreadPoolExecutor(max_workers=20) as pool:
            futures = {pool.submit(self._probe, t): t for t in targets}
            for future in futures:
                result = future.result()
                if result:
                    results.append(result)
        return results

    def _probe(self, host: str, ports: List[int] = None) -> List[Dict]:
     found = []
     http_ports  = [80, 8080, 8000, 3000, 5000]
     https_ports = [443, 8443, 4443]
     
     if ports:  # use nmap discovered ports
         http_ports  = [p for p in ports if p not in https_ports]
         https_ports = [p for p in ports if p in https_ports]
     
     for port in http_ports:
         url = f"http://{host}:{port}" if port != 80 else f"http://{host}"
         result = self._try_url(url)
         if result: found.append(result)
     
     for port in https_ports:
         url = f"https://{host}:{port}" if port != 443 else f"https://{host}"
         result = self._try_url(url)
         if result: found.append(result)
    
     return found
 
def _try_url(self, url: str) -> Dict | None:
    try:
        r = httpx.get(url, timeout=8, follow_redirects=True,
                      verify=False, headers={"User-Agent": "Mozilla/5.0"})
        return {
            "url": url,
            "status_code": r.status_code,
            "title": self._extract_title(r.text),
            "server": r.headers.get("server", ""),
            "live": True
        }
    except:
        return None

def _extract_title(self, html: str) -> str:
    import re
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)       
    return match.group(1).strip()[:100] if match else ""

# ─────────────────────────────────────────
# AGGREGATOR AGENT
# ─────────────────────────────────────────

class AggregatorAgent:
    """Merges, deduplicates, and normalizes all agent outputs."""

    def aggregate(self, target: str, subdomains, nmap_results,
                  dns_records, live_urls, spidered_urls) -> ReconResult:
        # Resolve IPs from subdomains
        ips = set()
        for sub in subdomains:
            try:
                ip = socket.gethostbyname(sub)
                ips.add(ip)
            except socket.gaierror:
                pass

        return ReconResult(
            target=target,
            subdomains=sorted(set(subdomains)),
            ips=sorted(ips),
            open_ports=nmap_results,
            dns_records=dns_records,
            live_urls=live_urls,
            spidered_urls=sorted(set(spidered_urls))
        )

# ─────────────────────────────────────────
# ORCHESTRATOR
# ─────────────────────────────────────────

class OrchestratorAgent:

    def __init__(self):
        self.subfinder   = SubfinderAgent()
        self.nmap        = NmapAgent()
        self.dns         = DNSDumpsterAgent()
        self.zap         = OWASPZapAgent()
        self.httpx       = HttpxAgent()
        self.aggregator  = AggregatorAgent()

    def run(self, domain: str, output_file: str = "recon_output.json") -> ReconResult:
        print(f"\n{'='*50}")
        print(f" Layer 1 Recon — Target: {domain}")
        print(f"{'='*50}\n")

        # Phase 1: Parallel discovery (subfinder + DNS)
        with ThreadPoolExecutor(max_workers=3) as pool:
            f_sub = pool.submit(self.subfinder.run, domain)
            f_dns = pool.submit(self.dns.run, domain)
            subdomains  = f_sub.result()
            dns_records = f_dns.result()

        # Phase 2: Port scan discovered hosts
        all_targets = list(set([domain] + subdomains))
        nmap_results = self.nmap.run(all_targets)

        # Phase 3: Probe live URLs
        live_urls = self.httpx.run(all_targets)
        live_url_list = [u["url"] for u in live_urls if u.get("live")]

        # Phase 4: Spider live URLs
        spidered_urls = self.zap.run(live_url_list)

        # Phase 5: Aggregate
        result = self.aggregator.aggregate(
            domain, subdomains, nmap_results,
            dns_records, live_urls, spidered_urls
        )

        # Save output
        with open(output_file, "w") as f:
            json.dump(asdict(result), f, indent=2)

        print(f"\n[✓] Recon complete. Output saved to {output_file}")
        self._print_summary(result)
        return result

    def _print_summary(self, r: ReconResult):
        print(f"\n{'─'*40}")
        print(f"  Subdomains found : {len(r.subdomains)}")
        print(f"  IPs resolved     : {len(r.ips)}")
        print(f"  Hosts scanned    : {len(r.open_ports)}")
        print(f"  Live URLs        : {len(r.live_urls)}")
        print(f"  Spidered URLs    : {len(r.spidered_urls)}")
        print(f"{'─'*40}\n")

# ─────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────

if __name__ == "__main__":
    orchestrator = OrchestratorAgent()
    orchestrator.run("google.com")