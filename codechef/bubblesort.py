def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                x=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=x

 
arr = [7, 2, 8, 4, 5, 2, 9,39 ,37 ,21 ,7 ,36 ,2]
 
bubblesort(arr)
 
for i in range(len(arr)):
    print("%d" %arr[i])