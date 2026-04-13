n = int(input())
n_list = list(map(int,input().split()))
n_dict = {}
for i in n_list:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

x = int(input())
x_list = list(map(int,input().split()))
result = []
for i in x_list:
    if i not in n_dict:
        result.append(0)
    else:
        result.append(n_dict[i])
print(*result)