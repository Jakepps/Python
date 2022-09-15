#10
#нашел прикольную функцию вывода
#def print_set(some_set):
#    print(len(some_set))
#    print(*[str(item) for item in sorted(some_set)]) 
#N, M = [int(s) for s in input().split()]
#A_colors, B_colors = set(), set()
#for i in range(N):
#    A_colors.add(int(input()))
#for i in range(M):
#    B_colors.add(int(input()))
     
#print_set(A_colors & B_colors)
#print_set(A_colors - B_colors)
#print_set(B_colors - A_colors)
#11
actions = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}
 
file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)
 
for i in range(int(input())):
    action, file = input().split()
    if actions[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')