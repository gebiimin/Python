#도전문제

n = int(input("정수를 입력하시오: "))
fact = 1
for i in range(-n, 0):
    fact = fact * i
print(n, "!은", fact, "이다.")