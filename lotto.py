import random

result=[]

money = input("얼마를 샀나요? => ")

for i in range(int(money)):
    while len(result) < 6:
        num = random.randint(1,45)

        if num not in result:
            result.append(num)

    result.sort()
    print(result)
    result.clear()
