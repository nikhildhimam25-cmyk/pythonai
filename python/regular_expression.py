import re
# exp="[6-9]{1}\d{9}"
pri="my name nikhil my phone number is 8580578066 my email id is nikhildhimam25@gmail.com and anurag email is anurag@hotmail.com and ansh email is anshmalot@yahoo.in" 
# print(re.findall(pattern=exp,string=pri))

em='[a-zA-Z0-9_.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+'
print(re.findall(pattern=em,string=pri))
s1=re.sub(pattern=em,repl="welcome",string=pri)
print(s1)