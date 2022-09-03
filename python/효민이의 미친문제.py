import random
import sympy as sy
import numpy as np

cnt=0
list1=[]
ascore=0
bscore=0

cnt=0

for i in range (-20,21):
        list1.append(i) 
print("카드를 뽑겠습니다.")

number=random.sample(list1,15)#sample함수:random.sample(sequence, k) sequence에서 지정한 숫자만큼의 요소들을 랜덤으로 뽑아 리스트로 반환해주는 함수
number.sort()
print("새로운 카드 모음입니다.")
print(number)

yes_or_no=input("내기를 시작하시겠습니까?(y/n) :")

if(yes_or_no=='y'):
    print("내기를 시작합니다.")
if(yes_or_no=='n'):
    print("내기를 종료합니다.")
    exit()

while True:

 if(ascore<=3)and(bscore<=3):
      cnt+=1
      print("%d번째 게임을 시작합니다" %cnt)
    
      number2=random.sample(number,2)
      a,b=map(int,number2)
    
      new_number=[k for k in list1 if k not in number ]#리스트-리스트 구문
      number3=random.sample(new_number,3)
      c,d,e=map(int,number3)

      if(c!=0):
    
        x=sy.symbols('x')#x를 변수로 사용함을 선언

        f =  c * x ** 2 + d * x + e
        F=sy.integrate(f,x)
        print(F)
    
     
        print("첫번째 변수값을 뽑겠습니다:{0}".format(a))
        print("두번째 변수값을 뽑겠습니다.:{0}".format(b))

        Igl=(F.subs(x,a)-F.subs(x,b)).evalf()
        print("두 수 사이에 존재하는 모든 값들의 합은 다음과 같습니다. :{0}".format(Igl))
        if(Igl>0):
            print("봉담이님이 이기셨습니다.")
            ascore+=1
            print("현재 스코어 {0}:{1}".format(ascore,bscore))
            if(ascore<3)and(bscore<3):
                print("잠시 후 다음 게임이 시작됩니다.")
            
        if(Igl<0):
            print("김내기님이 이기셨습니다.")
            bscore+=1
            print("현재 스코어 {0}:{1}".format(ascore,bscore))
            if(ascore<3)and(bscore<3):
                print("잠시 후 다음 게임이 시작됩니다.")
            
        if(ascore==3)or(bscore==3):
            print("게임이 종료되었습니다. 최종스코어 {0}:{1}".format(ascore,bscore))
        
        if(ascore==3):
            per1=(ascore/cnt)*100
            print("봉담이님이 최종승리 하셨습니다. 승률 : {0}%%".format(per1) )
            print("이용해 주셔서 감사합니다.")
            break
        
        if(bscore==3):
            per2=(bscore/cnt)*100
            print("김내기님이 최종승리 하셨습니다. 승률 : {0}%%".format(per2) )
            print("이용해 주셔서 감사합니다.")
            break                   

    

 
    
   

    

















                



         
  


 
   
   



    
    








