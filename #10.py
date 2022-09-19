import string
string.punctuation
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
#ACTION_PERMISSION = {
#    'read': 'R',
#    'write': 'W',
#    'execute': 'X',
#}
 
#file_permissions = {}
#for i in range(int(input())):
#    file, *permissions = input().split()
#    file_permissions[file] = set(permissions)
 
#for i in range(int(input())):
#    action, file = input().split()
#    if ACTION_PERMISSION[action] in file_permissions[file]:
#        print('OK')
#    else:
#        print('Access denied')
#12
namefile='C:/Users/Артём/source/repos/Jakepps/Python/test.txt'
num_words = 0
with open(namefile, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

with open(namefile) as f:
    flat_list=[word for line in f for word in line.split()]
out=(" ".join(flat_list))

for p in string.punctuation:
    if p in out:
        out=out.replace(p,'')

counter = {}
for i in range(num_words):
    line = out.split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
         
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))