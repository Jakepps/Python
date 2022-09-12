#7
#a=[int(i) for i in input().split()]
#for i in range(1,len(a)):
#    if a[i] > a[i-1]:
#        print(a[i])
#8
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))