from tkinter import *

root = Tk()
root.title("YD GUI")
root.geometry("640x480+300+100")

# label 글자, 이미지를 보여주는 정도
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui/check.png")
label2 = Label(root, image=photo)
label2.pack()

# 버튼 클릭시 label1 텍스트 변경
def changeLabel1():
    label1.config(text="또 만나요")

btn1 = Button(root, text="클릭", command=changeLabel1)
btn1.pack()

# 버튼 클릭시 label2 이미지 변경
def changeLabel2():

    # 이미지가 삭제 된다면 GC 가비지 컬렉션으로 인해 이미지 삭제
    # 필요없는것은 가비지 컬렉션이 자동으로 삭제 그렇게 하고 싶지 않을 경우 전역 변수로 설정
    global photo2
    photo2 = PhotoImage(file="gui/yes.png")
    label2.config(image=photo2) 
btn2 = Button(root, text="이미지 변경 클릭", command=changeLabel2)
btn2.pack()

root.mainloop()