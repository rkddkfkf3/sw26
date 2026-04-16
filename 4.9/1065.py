N = int(input())
count = 0

for i in range(1, N+1):

    if i < 100:
        count += 1

    else:
        s = str(i)

        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            count += 1

print(count)