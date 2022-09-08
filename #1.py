#1
#b=int(input('b='))
##h=int(input('h='))
#S=(1/2)*b*h
#print('S=',S)
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