a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c

x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)

if D > 0:
	print("Первый корень = ", x1)
	print("Второй корень = ", x2)

if D == 0:
	x = -b / (2*a)
	print("Корень = ", x)

else:
	print("Уравнение не имеет корней")