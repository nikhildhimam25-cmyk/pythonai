import subprocess
import sys

def find_subdomains(domain):
    """
    Calls the subfinder binary and returns a list of discovered subdomains.
    """
    # The command we want to run: subfinder -d <domain> -silent
    command = ['subfinder', '-d', domain, '-silent']

    try:
        # Run the command, capture stdout and stderr, return as string (text=True)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Split the output by newlines and filter out any empty strings
        subdomains = [line.strip() for line in result.stdout.split('\n') if line.strip()]
        return subdomains

    except FileNotFoundError:
        print("Error: 'subfinder' binary not found.")
        print("Please ensure it is installed and added to your system's PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing subfinder: {e.stderr}")
        return []

if __name__ == "__main__":
    # Get user input
    target = input("enter url ")