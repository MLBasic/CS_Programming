import random

dice = random.randrange(6)+1  # 1 ~ 6 이 나온다
print("주사위 던지기 게임을 시작합니다. ")

if dice == 1:  
    print("주사위의 눈은 1 입니다. ")
elif  dice == 2:
    print("주사위의 눈은 2 입니다. ")
elif  dice == 3:
    print("주사위의 눈은 3 입니다. ")
elif  dice == 4:
    print("주사위의 눈은 4 입니다. ")
elif  dice == 5:
    print("주사위의 눈은 5 입니다. ")
else :
    print("주사위의 눈은 6 입니다. ")

print("게임이 종료되었습니다.")


    
