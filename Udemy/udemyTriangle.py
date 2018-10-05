s1 = int(input("enter side 1 "))
s2 = int(input("enter side 2 "))
s3 = int(input("enter side 3 ")	)
	
if s1==s2 and s2==s3:
    	print (" Equilateral triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print ("Isoscelse triangle")
else:
    print(" Scalene triangle")
