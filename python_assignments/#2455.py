#2455
people = 0     
max_people = 0 
for i in range(4):
    out_people, in_people = map(int, input().split())
    people = people - out_people
    people = people + in_people
    if people > max_people:
        max_people = people
print(max_people)