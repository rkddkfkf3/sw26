n = int(input())
dict = {} 
list0 = []

for i in range(n):
    name, status_ = input().split()
    dict[name] = status_

for j in dict:
    if dict[j] == 'enter' :
        list0.append(j)

list0.sort()
list0.reverse()
print(*list0, sep='\n')