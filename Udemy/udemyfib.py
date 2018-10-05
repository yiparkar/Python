n=50
f=0
pr=1
while f<n:
    t=f
    f=f+pr
    pr=t
    if f > 50:
        break
    print (f)

    