k = []
n = int(input())
for i in range(n):
  num = int(input())
  if num == 0:
    del k[-1]
  else:
    k.append(num)
add = 0
for i in k:
  add = add + i
print(add)