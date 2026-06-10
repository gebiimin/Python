from tkinter import *
import random

answer = random.randint(1,100) 

def guessing():
    guess = int(guessField.get()) 

    if guess > answer:
        msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else:
        msg = "정답!"
    resultLabel["text"] = msg # 메시지를 출력한다.
    guessField.delete(0, 5)