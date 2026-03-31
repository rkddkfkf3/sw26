m=int(input())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
start_day=4 #시작일이 목요일
for i in range (m-1):
    start_day+=days[i]

start_day%=7  #시작요일 맞추기 

print(f"{m}월".center(20))

print("일 월 화 수 목 금 토")
for i in range(start_day):
    print("   ", end="")

for day in range (1, days[m-1]+1):
    print(f"{day:2}", end=" ") #f string 줄 간격 

    if (start_day+day)%7==0:
        print()