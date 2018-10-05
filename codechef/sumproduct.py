def sumproduct(arr1,arr2):
    sum=0
    for i in range(len(arr1)):
        sum+= arr1[i]*arr2[i]
    print ("%d"%sum)

a=[10,40,62,10]
b=[20,50,70,10]

sumproduct(a,b)