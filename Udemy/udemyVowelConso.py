import re

v= raw_input("Enter letter ")

if re.search("[aeiou]",v):
    print("vowel")
else:
    print("Consonant")
