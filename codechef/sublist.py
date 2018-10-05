def is_sublist(f,s):
    if s == []:
        return True
    elif f==s:
        return True
    elif len(f)<len(s):
        return False
    flag = False
    for i in range(len(s)):
        for j in range (len(f)):
            if s[i] == f[j]:
                flag= True
                break
        if flag == False:
            break
    return flag
   
f= [3,6,4,8]
s1= [5,8]
s2=[4,6]

print (  is_sublist(f,s1))
print ( is_sublist(f,s2))
