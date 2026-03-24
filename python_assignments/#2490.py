#2490
for _ in range(3):          
    yut = input().split()
    count = 0
    for i in yut:          
        if i == '0':
            count += 1
    if count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
    else:
        print("E")