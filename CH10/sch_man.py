# 딕셔너리

mydict = {}   # 2099.1.1 "해맞이" // 2099.1.1  "과제"

while True:
    date = input("날짜를 입력하시오: ")
    if date == 'q':
        break
    job = input("일정을 입력하시오: ")
    if date not in mydict:
        mydict[date] = []   # {'2099.1.1':[]}
        mydict[date].append(job)  # {'2099.1.1':["해맞이"]}
    else :
        mydict[date].append(job)  # {'2099.1.1':["해맞이","과제"]}
        
print(mydict)
