phrase = input("문자열을 입력하시오: ")

acronym = ""

for word in phrase.upper().split():
    acronym += word[0] # 단어를 첫 글자만을 acronym에 추가한다.
print( acronym )