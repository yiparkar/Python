s= raw_input('enter string ')
c=0
d =0
for i in range(len(s)):
    if s[i].isalpha():
        c=c+1
    elif s[i].isdigit():
        d=d+1
print ("Letters ", c)
print ("Numbers ",d)