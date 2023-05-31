items = {'커피음료':7 , '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5}

while True:
    item = ''
    while item not in items.keys():
        item = input("물건의 이름을 입력하시오(모르면 '0'): ")
        if item=='0':
            print(items.keys())

    # 1,2,3,q 중의 하나의 입력 
    menu = input("재고확인 '1', 재고증가 '2', 재고감소 '3' 을 입력하세요 (종료는 'q') : " )
    if menu == '1':
        print(item, '의 재고는', items[item], '개 입니다.')
        
    elif menu == '2':
        cnt = int(input("몇개를 추가 입고하시겠습니까? : "))
        items[item] += cnt
        print(item, '의 재고는', items[item], '개 입니다.')
        
    elif menu == '3':
        cnt = int(input("몇개를 출고하시겠습니까? : "))
        items[item] -= cnt
        print(item, '의 재고는', items[item], '개 입니다.')
        
    elif menu == 'q':
        print("종료")
        break
    else :
        print("'1','2','3','q' 중의 하나의 문자로 다시 입력해주세요 ")
        
print("편의점 재고관리 시스템을 종료합니다. ")  
