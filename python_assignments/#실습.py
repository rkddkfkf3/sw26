#실습 1 오전/오후
import datetime
now=datetime.datetime.now()
if now.hour<12:
  print("현재 시간은 {HOUR}시로 오전입니다.".format(HOUR = now.hour))
else:
  print("현재 시간은 {HOUR}시로 오후입니다.".format(HOUR = now.hour))
#실습 2 윤년
year=int(input())

if (year%400==00) or ((year%4==0) and (not(year%100==0))):
  print("%d is a leap year" %year)
else:
  print("%d is not a leap year"%year)
