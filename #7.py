#7
#a=[int(i) for i in input().split()]
#for i in range(1,len(a)):
#    if a[i] > a[i-1]:
#        print(a[i])
#8
#def fib(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)
#print(fib(int(input())))
#9
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print("i=",best_i,"j=",best_j)