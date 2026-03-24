#2530
A, B, C = map(int, input().split())
D = int(input())
x = A*3600 + B*60 + C
x = (x + D) % 86400
hour = x // 3600
x %= 3600
minute = x // 60
second = x % 60
print(hour, minute, second)