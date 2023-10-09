from tkinter import * # tkinter module을 사용

root = Tk()

root.title("YD GUI") # 제목 설정
root.geometry("640x480+300+100") # 가로, 세로, x좌표, y좌표 설정
root.resizable(False, False) # x, y 크기 변경 불가

root.mainloop()
