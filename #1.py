import math
import random
#1
b=int(input('b='))
h=int(input('h='))
S=(1/2)*b*h
print('S=',S)
#2
g=int(input('g='))
if g % 4!=0:
   print('NO')
elif g % 100 == 0:
    if g % 400 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('YES')
#3
n=int(input('n='))
m=int(input('m='))
print(round(m/n))
#4
sum=0
n=1 
for i in 1, 3, 4, 7, 101, 2, 4, 5, 122, 14:
    print(i)
    sum +=i 
print(sum,end='.')
#5
a=input('Ввидите слово=')
first=a[0:len(a)//2]
c=a[len(a)//2:-1]
l=a[-1]
second=c+l
print(second+first)
#6
i = -1
k = -1
e = 1
max = 1 
while i != 0:
    i = int(input())
    if i == k:
        e += 1
    else:
        if e > max:
            max = e
            e = 0
    k = i
print(max)