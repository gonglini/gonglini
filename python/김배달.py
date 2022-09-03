import random
import time
from time import sleep
k3bag=0
k5bag=0
down=random.randint(1,100)
scratch=random.randint(1,100)
rain=random.randint(1,100)
trafic=random.randint(1,100)

a=0





n=int(input("몇KG 주문 하시겠습니까> :"))
time=int(input("현재 시각은 몇시 인가요?(00:00~24:59 사이로 입력하시오) :"))



while True:#닭배달의 최소 조건을 검사한후, 닭 봉지를 최대한 적게 챙기는 방향으로 들게 함
    if(time<22)and(time>4):
        if(n<110):
                if n%5==0:
                    k5bag=n//5
                    print("5kg %s봉지 배달 시작합니다."%k5bag)
                    
                else:
                    while True:
                        if n%5 != 0:
                            k5bag=n//5
                            n=n-3
                            k3bag += 1
                        else:
                            break
                    
                print("5kg {0}봉지,3kg {1}봉지 배달 시작합니다." .format(k5bag,k3bag))
               
                break
                    
    else:
        print("배달이 불가합니다.")
        exit()#exit()함수로 프로그램 종료를 하지 않으면 밑에 문단들이 실행되어서
      #배달을 할수없는데 배달을 시작함 
       
        


print("배달을 시작합니다.")
sleep(1)
               




    
if(time>=18):
         print("야간시간입니다. 넘어질 확률이 증가합니다.")
         sleep(1)
         y=1   
if(time<=5):
        print("야간시간입니다. 넘어질 확률이 증가합니다.")
        sleep(1)
        y=1        
                 
            
if(rain<=30):
            print("비가옵니다 넘어질 확률이 증가합니다.")
            r=1










while True:    #상황발생 확률
    if(trafic<=30):
            print("도로가 막힙니다. 넘어질 확률이 증가합니다.")
            sleep(2)
            a=0
            break
    if(time>=18):
                if(trafic<=60):
                    print("도로가 막힙니다. 넘어질 확률이 증가합니다.")
                    a=2
                    break
    if(time<=20):
                if(trafic<=60):
                    print("도로가 막힙니다. 넘어질 확률이 증가합니다.")
                    a=2
                    break             
                     
    if(time>=8):
                if(trafic<=60):
                        print("도로가 막힙니다. 넘어질 확률이 증가합니다.")
                        sleep(1)
                        a=2
                        break 
    
    if(time<=10):
                if(trafic<=60):
                        print("도로가 막힙니다. 넘어질 확률이 증가합니다.")
                        
                        sleep(1)
                        a=2
                        break 
    break 

while(True): #a,r,y는 각각 교통체증,비,야간시간대의 조건이 발생했을때만 생성되는 변수들 이걸로 조건문의 조건을 작성해본다.
    if(down<=90):#악조건 x 
            print("김배달씨가 넘어졌습니다.")
            if(scratch<=95):
                how_many3=random.randint(1,k3bag)
                k3bag=k3bag-how_many3
                print("남은 3kg 봉지들{0}".format(k3bag))
                sleep(1)    
            if(scratch<=90):
                how_many5=random.randint(1,k5bag)
                k5bag=k5bag-how_many3
                print("남은 5kg 봉지들{0}".format(k5bag))
                print("도착했습니다.")
                print("수고하셨습니다.")
                exit()      
            
            
            
    else:
            print("배달을 완료했습니다.")
            print("남은 봉지들 3kg{0},5kg{1}.".format(k3bag,k5bag))
            print("수고하셨습니다.")    
            exit()   
    if(a==0)or(a==1):#교통체증이 발생 했을때
            if(down<=90):
                print("김배달씨가 넘어졌습니다.")
                break
            elif(r==1):
                if(down<=90):#교통체증+우천
                    print("김배달씨가 넘어졌습니다.")    
                    break
    if(y==1)and((a==0)or(a==1))(r==1):#교통체증+우천+야간(110%임으로 100%확률로 넘어진다.)
                    print("김배달씨가 넘어졌습니다.")
                    break
            
    if(r==1):#우천
        if(down<=90):
            print("김배달씨가 넘어졌습니다.")
            break                
        elif(y==1):
            if(down<=80):#우천+야간
                print("김배달씨가 넘어졌습니다.")
                break
    if(y==1):#야간
        if(down>=50):
            print("김배달씨가 넘어졌습니다.")
            break

 
if(scratch<=35):
                how_many3=random.randint(1,k3bag)
                k3bag=k3bag-how_many3
                print("남은 3kg 봉지들{0}".format(k3bag))
                sleep(1)    
                if(scratch<=40):
                    how_many5=random.randint(1,k5bag)
                    k5bag=k5bag-how_many3
                    print("남은 5kg 봉지들{0}".format(k5bag))
                    print("도착했습니다.")
                    print("수고하셨습니다.")
                    exit()     



        

                    
                    
        
        
        
        
              
            
            
            
            
    
    

            

            
    
    
    
    
    
    
    
    


    





















































    
            
        
    
                   
                
       
        

                  
    


        


