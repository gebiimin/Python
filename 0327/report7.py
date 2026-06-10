#조건 제어 반복

Target = 2000
money = 1000
year = 0
rate = 0.07

while money < Target:
    money = money + money * rate
    year = year + 1
print(year, "년")