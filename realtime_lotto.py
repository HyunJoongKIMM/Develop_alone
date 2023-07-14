# import random
# import datetime

# result = []

# print("")
# money = input("얼마치 구입했나요? (숫자만 입력) ==> ")
# print("")

# print("############################################")
# for i in range(int(money)):
#     type(i)
#     while len(result) != 6:
#         num = random.randint(1, 45)
        
#         if num not in result:
#             result.append(num)

#     result.sort()
#     print(i+1, "번 쨰 번호 ==>", result)
#     result.clear()
# print("############################################")


import random

result = []
number_win = []
number_answer = [0,0]
number_rank = [0, 0, 0, 0, 0, 0]

money = input("얼마치 구입했나요? (숫자만 입력) ==> ")

print("############################################")
l = 0
while l <  7 :
    num = random.randint(1,45)

    if num not in number_win:
        number_win.append(num)
        l += 1

print("당첨 번호 ==>", number_win," + 보너스: ",number_win[-1])
print("############################################")

for i in range(int(money)):
    type(i)
    while len(result) != 6:
        num = random.randint(1, 45)
      
        if num not in result:
            result.append(num)

    result.sort()
    print(i+1, "번 쨰 번호 ==>", result)

    for j in result:
        for z in number_win:
            if z == j:
                if number_win[6] == j:
                    number_answer[1] += 1
                else:
                    number_answer[0] += 1

    if number_answer[0] == 6:
        print(" 1등 ")
        number_rank[0] += 1
    elif number_answer[0] == 5 and number_answer[1] == 1:
        print(" 2등 ")
        number_rank[1] += 1
    elif number_answer[0] == 5:
        print(" 3등 ")
        number_rank[2] += 1
    elif number_answer[0] == 4:
        number_rank[3] += 1
        print(" 4등 ")
    elif number_answer[0] == 3:
        print(" 5등 ")
        number_rank[4] += 1
    else:
        print(" 꽝 ")
        number_rank[5] += 1
    number_answer = [0,0]
    result.clear()
number_win.sort()
print("############################################")
print("1등 번호는 !! =>",number_win)
print("1등: ",number_rank[0]," 2등: ",number_rank[1]," 3등: ",number_rank[2]," 4등: ",number_rank[3]," 5등: ",number_rank[4]," 꽝: ",number_rank[5],)
print("############################################")