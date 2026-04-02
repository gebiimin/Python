n = int(input("숫자를 입력하시오: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0 , -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

