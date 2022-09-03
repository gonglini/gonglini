import os
import random
import time
import sympy as sy

num_card =[]
new_nums =[]
exp = 0
score =0
score2 =0

for i in range (-20,21):
    num_card.append(i) 

for j in range (0,15):
    k = random.choice(num_card)
    new_nums.append(k)
    num_card.remove(k)

new_nums.sort()

print("카드를 뽑겠습니다.\n")

time.sleep(1.0)

print("새로운 카드 모음 입니다.\n ", new_nums)


start = input("내기를 시작하시겠습니까? y / n :")

if start == 'y':
    print("\n내기를 시작합니다")

if start == 'n':
    print('게임을 종료합니다.')
    exit()

for i in range(1,6):


    print("\n%d 번째 게임을 시작합니다" %i)
    while True:
        a = random.choice(num_card)
        if a != 0:
            break
    b = random.choice(num_card)
    c = random.choice(num_card)
    
    num1 = random.choice(new_nums)
    new_nums.remove(num1)
    num2 = random.choice(new_nums)
    new_nums.remove(num2)

    if num1 >= num2:
        exp = num1
        num1 = num2
        num2 = exp

    x = sy.symbols('x') 
    f =  a * x ** 2 + b * x + b
    F = sy.integrate(f, x)

    print("생성된 함수는 다음과 같습니다." ,f)
    
    time.sleep(1.0)
    
    print("""\n 첫번 째 변수값을 뽑겠습니다.
    첫 번째 변수 값은 다음과 같습니다. : """, num1 )
    
    time.sleep(1.0) 
    print("""\n 두 번째 변수값을 뽑겠습니다.
    두 번째 변수 값은 다음과 같습니다. : """, num2 )


    
    result = F.subs(x, num2) - F.subs(x, num1)

    time.sleep(0.5)
     
    print("\n 두 수 사이에 존재하는 모든 함수값들의 합은 다음과 같습니다. : ", end = '')
    print(result, "\n")

    time.sleep(0.5)

    if result > 0:
        print ("봉담님이 승리하였습니다.")
        score +=1
        
    if result < 0:
        print ("김내기 님이 승리히였습니다")
        score2 +=1
    
    print("현재 스코어 %d : %d " %(score,score2))
    
    if i < 5:
        print("\n잠시후 다음 게임이 시작됩니다. ")
    
    time.sleep(2.5)
    os.system('clear')
    

print("\n 게임이 종료 되었습니다. 최종스코어 %d : %d " %(score,score2))

if score > score2:
    win = 20*score
    print ("\n 봉담님이 승리하였습니다. 최종 승률 %d 퍼센트" %win)
    print("\n이용해 주셔서 감사합니다.")
    time.sleep(2.0)

if score < score2:
    win = 20*score2
    print ("\n 김내기 님이 승리하였습니다 최종 승률 %d 퍼센트" %win)
    print("\n이용해 주셔서 감사합니다")
    time.sleep(2.0)