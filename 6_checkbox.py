from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

# 체크박스 : 체크박스 목록 중 여러개 선택 가능

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # 값을 저장해줘야 함
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리 (default)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()