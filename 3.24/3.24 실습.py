#숫자 출력:
print("#0부터 9까지 출력")
for i in range(10):
    print(i,end='')
print()
print("#1부터 10까지 출력")
for i in range(1,11):
    print(i,end='')
print()
print("#2부터 10까지 짝수만 출력")
for i in range(2,11,2):
    print(i,end='')

#이율구하기
year=0
balance=1000000
while balance <2000000:
    year=year+1
    balance=int(balance*1.05)
print("{}년 저금 하시면 {}원이 됩니다.".format(year,balance))
