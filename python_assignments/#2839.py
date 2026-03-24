#2839
n = int(input())
five = n // 5 
while five >= 0:
    remain = n - (five * 5)
    if remain % 3 == 0:
        three = remain // 3
        print(five + three)
        break
    five -= 1
else:
    print(-1)