txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words)

print("사용된 단어의 개수= ", len(unique))
print(unique)