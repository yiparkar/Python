min = 1500
max = 2700
n=[]
for i in range(1500,2700):
    if (i%7==0) and (i%5==0):
            n.append(str(i))
print(','.join(n))
