#Lab: 파이 계산하기

divisor = 1.0
divident = 4.0
sum = 0.0
LoopCount = int(input("반복횟수: "))

while(LoopCount > 0):
    sum = sum + divident / divisor
    divident = -1.0 * divident
    divisor = divisor + 2
    LoopCount = LoopCount - 1
print("Pi = %f" % sum)