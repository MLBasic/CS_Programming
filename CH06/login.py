real_password = "pythonisfun"

password = ""

while True:
    password = input("암호를 입력하세요 : ")
    if password == real_password:
        break

print("로그인 성공")
