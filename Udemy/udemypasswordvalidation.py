import re

p= raw_input (" Enter password ")

x=True

while x:
    if len(p)<6 and len(p)>16:
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        x=False
        print("Valid password")
        break
if x:
    print ("Invalid password")