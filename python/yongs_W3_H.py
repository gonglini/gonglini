import random
import time

user1 = []
user2 = []

user1_num = 0
user2_num = 0
num = ['1','2','3','4','5','6','7','8','9']

while True:
    n = int(input("1~9사이의 정수 N을 입력해주세요. : "))
    
    if n >= 1 and n < 10:
        print("\n게임을 시작합니다")
        time.sleep(2.0)
        break
    else:
        print("\n잘못된 입력입니다.\n")
        time.sleep(1.5)

for i in range (0,n):
    user1.append(random.choice(num))
    user2.append(random.choice(num))

result1 = int("".join(user1))
result2 = int("".join(user2))

print("\n사용자1 의 숫자는 다음과 같습니다", result1)
time.sleep(1)
print("\n사용자2 의 숫자는 다음과 같습니다", result2)
time.sleep(2.0)

if result1 > result2:
    print("\n%d 대 %d 로 사용자1이 승리했습니다" %(result1,result2))
if result1 < result2:
    print("\n%d 대 %d 로 사용자2가 승리했습니다" %(result1,result2))

time.sleep(1)
print("이용해 주셔서 감사합니다")
time.sleep(1.5)