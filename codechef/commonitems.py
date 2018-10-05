def common(f,s):
    r=[]
    if s == []:
        return r
    elif f==s:
        return f
    
    for i in range(len(s)):
        for j in range (len(f)):
            if s[i] == f[j]:
                r.append(s[i])
                break
        
    return r

color1 = ["Red", "Green", "Orange", "White"] 
color2 = ["Black", "Green", "White", "Pink"]

r=common(color1,color2)

print(r)
print("easy method")
print(set(color1)& set (color2))
print("Difference from list two")
print(list(set(color1)- set(color2)))

print("Max")

ls=[1,2,-8,0]
print(ls)
print(max(ls))