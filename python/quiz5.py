import os
import time


def all_coin(coin =0):
    cnt =0
    height = 0
    R_height =0
    length = 0
    R_length =0
    area = 0
    mi_area=0
    move =[[0]* 2 for x in range (9) ]

    get= int(input("1m^2당 채굴할수 있는 코인을 입력하세요 : "))

    while cnt <= 7:
        i= int(input("\n움직일 방향을 입력하세요: "))
        j= int(input("\n원하는 길이를 입력하세요: "))
        move[cnt][0] = i
        if i == 1:
            move[cnt][1] =j
            height += j
            R_height += j
        elif i ==2:
            move[cnt][1] =j
            height -= j
        elif i ==3:
            move[cnt][1] =j
            length += j
            R_length += j
        elif i ==4:
            move[cnt][1] =j
            length -= j
        else:    
            print("\n잘못된 경로입니다. 3초후 종료됩니다")
            time.sleep(3)
            exit()
        cnt += 1

    if height != 0 or length != 0:
        print("\n올바른 도형이 아닙니다, 3초후 종료됩니다.")
        time.sleep(3)
        exit()

    area = R_height*R_length

    for i in range(0,8):

        if move[i][0]== 4 and move[i+1][0] == 1:
            mi_area += move[i][1] * move[i+1][1]
    
        if move[i][0]== 2 and move[i+1][0] == 4:
            mi_area += move[i][1] * move[i+1][1]
    
        if move[i][0]== 3 and move[i+1][0] == 2:
            mi_area += int(move[i][1]) * int(move[i+1][1])

        if move[i][0]== 1 and move[i+1][0] == 3:
            mi_area += move[i][1] * move[i+1][1]


    area -= mi_area


    coin = area*get

    print("\n전체 넓이는 %d 제곱미터 입니다" %area)
    print("\n전체 채굴 가능한 코인의 수는 %d 개 입니다" %coin)

    print("\n3초 후 채굴을 시작합니다.")
    time.sleep(3)

    return int(coin)



def mining(coin = all_coin()):

    coins = coin
    mined_coin = 0
    rainy_day =0
    mining_day =0
    day = 0

    os.system('clear')
    print("\n채굴을 시작합니다")
    time.sleep(1)
    while coin > 0:
        day += 1
        time.sleep(0.05)
        if day % 3 == 0:
            rainy_day +=1
            if coin >=500: 
                coin-= 500
            else:
                coin = 0
            print("\n비가 오는 관계로 채굴을 하지 못하였습니다")
            print("\n땅이 무너져 내려 채굴가능한 코인수가 줄어 듭니다. 현재 채굴가능한 코인의 수: %d" %coin) 
        else:
            mining_day +=1
            if coin >= 300:
                coin -=300
                mined_coin += 300
            else:
                mined_coin += coin
                coin = 0
            print("\n\n코인을 채굴하였습니다. 현재까지 채굴한 코인의 수 : %d , 채굴가능한 남은 코인의 수 : %d" %(mined_coin, coin))
    
    lost_coin = rainy_day * 500
    time.sleep(2.5)
    os.system('clear')
    print("\n채굴을 완료하였습니다")
    time.sleep(1)
    print("\n처음 채굴가능 한 코인의 수 : %d" %coins)
    time.sleep(0.8)
    print("\n총 채굴한 코인의 수 : %d" %mined_coin)
    time.sleep(0.8)
    print("\n비로 인한 손실된 코인의 수 : %d: " %lost_coin)
    time.sleep(0.8)
    print("\n비가 온 총 날짜 수 : %d: " %rainy_day)
    time.sleep(0.8)
    print("\n채굴이 가능했던 총 날짜 수 : %d: " %mining_day)
    time.sleep(0.8)
    print("\n채굴에 걸린 총 날짜 수 : %d: " %day)
    time.sleep(1.5)
    print("\n수고하셨습니다.")
    time.sleep(2)
    exit()