# Quiz) tkinter를 이용한 메모장 프로그램을 만드시오

# [GUI 조건]
# 1. title : 제목 없음 - Mac 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤바 넣기
from tkinter import *

root = Tk()
root.title("Mac 메모장")
root.geometry("640x100+300+100")
root.resizable(True, True)

def file_open():
    txt.delete("1.0", END)
    with open("gui/mynote.txt", "r", encoding="utf8") as f:
        content = f.read()
        txt.insert(END, content)
    

def file_save():
    content = txt.get("1.0", END)
    with open("gui/mynote.txt", "w", encoding="utf8") as f:
        f.writelines(content)


menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()