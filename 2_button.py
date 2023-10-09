from tkinter import * # tkinter module을 사용

root = Tk()
root.title("YD GUI") # 제목 설정

btn1 = Button(root, text="버튼1") # 버튼 위젯 생성
btn1.pack() # 화면 노출

btn2 = Button(root, padx=5, pady=10, text="버튼2") # pad == padding : 공간 설정 (공간에 따라 크기 달라짐)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width, height 고정 크기
btn4.pack()

# mac 배경색 적용 안됨
btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg : 글자색, bg : 배경색
btn5.pack()

photo = PhotoImage(file="gui/check.png") # 이미지 호출 file="location"
btn6 = Button(root, image=photo) # 버튼에 이미지 삽입
btn6.pack()

# click event
# 1. 함수 생성
def btncmd():
    print("버튼 클릭되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) # command = 함수 호출
btn7.pack()

root.mainloop()
