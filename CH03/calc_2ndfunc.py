a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

r = b**2-4*a*c

x1 = (-b + r**0.5)/(2*a)
x2 = (-b - r**0.5)/(2*a)

print("2개의 근은", x1, x2, "입니다. ")
