m = int(input("m "))
n = int(input("n "))
arr = [[0 for col in range(m)] for row in range (n)]
for i in range (n):
    for j in range (m):
        arr[i][j]= i*j

print(arr)
