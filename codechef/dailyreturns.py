def dailyreturns(arr):
    for i in range(len(arr)-1):
        print (float(arr[i+1])/float(arr[i])-1.0)*100.0
        
        
a=[10,20,30,40,50,60]
dailyreturns(a)