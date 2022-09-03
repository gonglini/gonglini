import os
import time
import random

cnt=1
num1= 0
num2 =0
score1 =0
score2 =0

dice = ['1', '2', '3', '4', '5', '6']

while True:
    print("%d 번째 게임을 시작합니다" %cnt)
    time.sleep(1)
    cnt+=1

    hyo = []
    yong = []
    for i in range(0,2):
        hyo.append(random.choice(dice))
        yong.append(random.choice(dice))

    for i in range(0,2):
        num1 += int(hyo[i])
        num2 += int(yong[i])
    
    print("\nhyo의 주사위 점수 : 눈금 결과 " ,hyo, "눈금의 합 : %d \n" %num1)
    time.sleep(1)
    print("\nyong의 주사위 점수 : 눈금 결과 " ,yong, "눈금의 합 : %d" %num2)

    if num1 > num2:
        score1 +=3
        print("hyo님이 승리하였습니다")
        print("\n현재스코어 %d : %d" %(score1, score2))
        time.sleep(1)
        os.system('clear')

    
    if num1 < num2:
        score2 += 3        
        print("yong님이 승리하였습니다")
        print("\n현재스코어 %d : %d" %(score1, score2))
        time.sleep(1)
        os.system('clear')

    if num1 == num2:
        print("동점입니다")
        time.sleep(1)
        os.system('clear')

    if score1 > 10 or score2 > 10:
        if score1 > 10:
            print("\n게임이 종료 되었습니다. 승자 = hyo")
            print("\n스코어 %d : %d" %(score1, score2))
        if score2 > 10:
            print("\n게임이 종료 되었습니다. 승자 = yong")
            print("\n스코어 %d : %d" %(score1, score2))
        break