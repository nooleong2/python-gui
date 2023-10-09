from tkinter import *

root = Tk()
root.title("YG GUI")
root.geometry("640x480+300+100")

# 글자를 입력할 수 있는 text 와 entry
# text = textarea (여러 줄)
# entry = input (한 줄)
txt = Text(root, width=30, height=5) # Text 위젯 생성
txt.pack()
txt.insert(END, "미리 들어가 있는 값") # 힌트용으로 사용하는 디폴트 값이라고 생각하면 됨

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력합니다")

# 버튼 클릭 시 text와 entry 값 가져오기 / 삭제하기
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0 번째 column 위치 ~ 끝까지
    print(e.get()) # entry는 get만 적어주면 됨

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()