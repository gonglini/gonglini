
cnt=0
valuessss=[]
value=[]
values=[]
real_height=0
real_length=0
directions_list=[]
lengths_list=[]
total_length=0
total_height=0
total_length_list=[]
total_height_list=[]
sum1=0
sum2=0
coins=0
loss=0
loss_day=0
coin=int(input("코인수를 입력하세요")) #코인 개수
for i in range(8):
    value=input().split()
    values.append(value)
    


for d in values:
    direction=d[0]
    directions=int(direction)
    directions_list.append(directions)
print(directions_list)

for h in values:
    length=h[1]
    lengths=int(length)
    lengths_list.append(lengths)
print(lengths_list)


for z in directions_list:#big box 
    if (z==1)or(z==2):#직사각형은 마주보는 두변의 길이가 같다.
        for g in lengths_list:
            sum1=sum1+g #a=+b 와 a=a+b는 같지않다
            
 
    if (z==3)or(z==4):#직사각형은 마주보는 두변의 길이가 같다.
        for k in lengths_list:
            sum2=sum1+k

big_width=sum1/2
big_height=sum2/2
big_square=big_width*big_height
print(big_square)


for m in values:
    valuess=m[1]
    valuesss=int(valuess)
    valuessss.append(valuesss)

max_side=max(valuessss)
min_side=min(valuessss)

print(max_side)
print(min_side)

first_small_square=max_side*min_side

indexno_max_side=valuessss.index(max_side)
where_is_indexing_value1=valuessss[indexno_max_side+2]
where_is_indexing_value2=valuessss[indexno_max_side+3]

second_small_squae=where_is_indexing_value1*where_is_indexing_value2


total_area_of_land=big_square-(first_small_square+second_small_squae)

possiblely_coin=total_area_of_land*coin

print("채굴가능한 코인개수는{0}이다.".format(possiblely_coin))

first_possible_coin=possiblely_coin

while True:
    cnt=cnt+1
    if(cnt%3!=0):
        possiblely_coin=possiblely_coin-300 #남은 코인의 개수
        coins=coins+300 #채굴한 코인의 개수
        print("{0}일차 채굴을 완료했습니다.".format(cnt))
        print("현재 채굴한 코인의 개수:{0} 채굴가능한 코인 개수{1}".format(coins,possiblely_coin))
    if(cnt%3==0):
            possiblely_coin-500
            loss=loss-500
            loss_day=loss_day+1


    if(possiblely_coin<=0):
        print("처음 채굴가능 했던 코인의 수 : {0}".format(first_possible_coin))
        print('총 채굴한 코인의 개수 : {0}'.format(coins))
        print('비로 인해 손실된 코인의 수 :  {0}'.format(-loss))
        print("비가 온 총 날짜수 : {0}".format(loss_day))
        break
    


    




        
   
    
    












           



            

            
        
   







            
            



            




       
                




                                            




 










  



        
   
    
        

