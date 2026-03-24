#2455
train =0
max_train = 0
for i in range(4):
    a,b = map(int,input().split())
    train -=a
    train +=b
    if max_train < train:
        max_train = train
print(max_train)