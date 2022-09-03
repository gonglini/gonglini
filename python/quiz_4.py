import os
import random
import time


small_pkg = 0
big_pkg = 0
cnt = 1
slip = 0
rain = 30
traffic_jam = 30
dice = []
kg =0

for i in range(1,101):
    dice.append(i)

while True:
    chicken = int(input("배달할 닭의 양을 입력하시오.: "))
    clock = int(input("\n현재 시각은 몇시 인가요? "))
    
    if chicken >110:
        kg = 1

    while chicken >= 0 :
        if chicken % 5 == 0 :  # 5의 배수이면
            big_pkg += (chicken // 5)
            chicken -= big_pkg * 5  # 5로 나눈 몫을 구해야 정수가 됨
            break
        chicken -= 3  
        small_pkg += 1 
    

    if kg ==1 or chicken >0 :
        print("배달할 수 없습니다. 다시 입력해주세요. \n")
        time.sleep(1)

    if clock < 22 and clock > 4:
        print("\n배달 가능")
        time.sleep(1)
        break
    else:
        print("해당시간에는 서비스를 지원하지 않습니다. 다시 입력해주세요. \n")


small_pkg_ori = small_pkg
big_pkg_ori = big_pkg

print("\n 5kg 봉지 %d 개와 3kg 봉지 %d개 만큼 가져갑니다" %(big_pkg, small_pkg))

time.sleep(2.0)
os.system('clear')

print("\n배달을 시작합니다.")
time.sleep(1)

if (clock >= 8 and clock <= 10) or (clock >= 18 and clock <=20):
    print("\n출퇴근 시간대 입니다. 교통체증 확률이 증가합니다")
    time.sleep(1)
    traffic_jam = 60
if (clock >= 18 or clock <= 5):
    print("\n야간 시간대 입니다. 넘어질 확률이 증가합니다")
    time.sleep(1)
    slip += 30

for i in range(0,2):
    num = random.choice(dice)

    if num <= rain and cnt == 1:
        print("\n비가옵니다. 넘어질 확률이 증가합니다")
        slip += 30
        time.sleep(1.0)
    if num <= traffic_jam and cnt == 2:
        print("\n교통체증이 발생했습니다. 넘어질 확률이 증가합니다")
        slip += 30
        time.sleep(1.0)
    cnt += 1

time.sleep(1)

num = random.choice(dice)

if num <= slip:
    print("\n넘어졌습니다!")
    time.sleep(1)
    if small_pkg >0: 
        for i in range(0,small_pkg):
            num = random.choice(dice)
            if num <= 35:
                small_pkg -= 1
        if small_pkg < small_pkg_ori:
            print("\n작은 봉지들이 찢어졌습니다. 남은 작은 봉지수 : %d." %small_pkg)
            time.sleep(1.0)
        else:
            print("\n 다행히도 작은 봉지들은 멀쩡했습니다")
            time.sleep(1.0)

    
    if big_pkg >0: 
        for i in range(0,big_pkg):
            num = random.choice(dice)
            if num <= 40:
                big_pkg -= 1
        if big_pkg < big_pkg_ori:
            print("\n 큰 봉지들이 찢어졌습니다. 남은 큰 봉지수 : %d." %big_pkg)
            time.sleep(1.0)
        else:
            print("\n 다행히도 큰 봉지들은 멀쩡했습니다")
            time.sleep(1.0)

chicken = small_pkg * 3 + big_pkg * 5

print("\n도착했습니다. 배달한 봉지수는 각각 3kg  %d 개, 5kg  %d 개 입니다." %(small_pkg, big_pkg))
time.sleep(0.5)
print("\n 배달한 총 치킨의 양은 %dkg 입니다." %chicken)
time.sleep(0.5)
print("\n수고하셨습니다.")
time.sleep(2)

    