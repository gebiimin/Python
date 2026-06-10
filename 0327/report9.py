#else가 있는 while 루프

i = 0

while i < 3:
    print("루프 안쪽")
    i = i + 1
else:
    print("else 부분")