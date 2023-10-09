from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

# 라디오 버튼 (목록 중 하나만 선택 가능)
Label(root, text="메뉴를 선택하세요").pack() # 값이 바뀌지 않을 경우 변수 없이 사용 해도 됨

# 목록이 그룹으로 묶여 있어야 됨 (여러개 중 하나를 선택하는것이기 때문)
burger_var = IntVar() # int형으로 값을 저장

btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() # 기본 값 설정
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 추가해주세요").pack()
drink_var = StringVar() # String형으로 값 저장
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select() # 기본 값 설정
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택 된 라디오 목록의 값(value) 출력
    print(drink_var.get()) # 음료수 중 선택 된 라디오 목록의 값(value) 출력

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()