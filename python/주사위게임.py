import random
import os
alist=[]
blist=[]
ascore=0
bscore=0
cnt=0
yesorno=input("게임을 시작 하시겠습니까? (y/n)")
if yesorno=='y':
    print("주사위 게임을 시작합니다.")
if yesorno=='n':
    print("주사위 게임을 종료합니다.")
    exit()       
  
while True:
        if (ascore<10)and(bscore<10):
            cnt+=1
            a1list=[]
            b1list=[] 
            print("%d번째 게임을 시작합니다."%cnt)        
            for i in range(2):
                alist.append(random.randint(1,6))
                blist.append(random.randint(1,6))
                plus1=sum(alist)
                plus2=sum(blist)  
           
            if(plus1%2==0):
                    ascore+=3               
                    print('효민이의 주사위 점수 : 눈금 결과:{0}, 눈금의 합 :{1},스코어:{2}'.format(alist,plus1,ascore))
            
            else:
                 print('효민이의 주사위 점수 : 눈금 결과:{0}, 눈금의 합 :{1},스코어:{2}'.format(alist,plus1,ascore))        

            if(plus2%2==0):
                    bscore+=3
                    print('정용이의 주사위 점수 : 눈금 결과:{0}, 눈금의 합 :{1},스코어:{2}'.format(blist,plus2,bscore))
            else:
                 print('정용이의 주사위 점수 : 눈금 결과:{0}, 눈금의 합 :{1},스코어:{2}'.format(blist,plus2,bscore))     

            if(ascore>10)and(bscore<10):
                 print("효민이 승")
                 break
            if(bscore>10)and(ascore<10):
                 print("정용이 승")  
                 break
            if(bscore>10)and(ascore>10):
                while True:
                    for i in range(2):
                     alist.append(random.randint(1,6))
                     blist.append(random.randint(1,6))
                     plus1=sum(alist)
                     plus2=sum(blist)
                     if(ascore>10)and(bscore<10):
                        print("효민이 승")
                        
                     if(bscore>10)and(ascore<10):
                         print("정용이 승")  