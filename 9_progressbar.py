import tkinter.ttk as ttk # progressbar 도 ttk에 존재
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 계속 움직임
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 채워 짐
progressbar.start(10) # 프로그레스 바 시작 10ms 마다 움직임
progressbar.pack()



def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text="stop", command=btncmd)
btn.pack()

# for 를 이용한 progress bar 세팅
import time

p_var = DoubleVar() # 소수점 까지 저장
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar2.pack()

# 버튼 클릭 시 프로그레스 바 시작
def btncmd2():
    for i in range(1, 101): # 1 ~ 100 까지
        time.sleep(0.01) # 0.01초 대기
        p_var.set(i) # p_var 값 세팅
        progressbar2.update() # 화면에 계속 찍어주기 위해 업데이트 작성

        print(p_var.get()) # 값 출력


btn2 = Button(root, text="start", command=btncmd2)
btn2.pack()


root.mainloop()