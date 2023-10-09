import tkinter.ttk as ttk # combo box는 다른 곳에 있기때문에 import 사용
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height = 목록 몇개 보여줄 지
combobox.set("카드 결제일") # 최초 목록 제목 설정, 버튼 클릭을 통한 값 설정 가능
combobox.pack()

# 읽기 전용, 콤보 박스 내용 수정 불가능
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # index 0 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택 값 출력
    print(readonly_combobox.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()