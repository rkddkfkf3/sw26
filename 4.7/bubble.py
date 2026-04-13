a=[8,4,9,5]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
for j in range(len(a)-2):
    if a[j] > a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
for x in range(len(a)-3):
    if a[x]>a[x+1]:
        a[x],a[x+1]=a[x+1],a[x]
print(a)