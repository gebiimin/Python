num = int(input("Enter a number: "))
sum = 1

for i in range(1, num + 1):
    sum *= i
    if i < 4:
        print(i, num)

print(num,"! = ",)