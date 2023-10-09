from tkinter import *

root = Tk()
root.title("YD GUI")
root.geometry("640x480+300+100")

# 리스트 박스
# selectmode = extended(여러개 선택), single(하나 선택)
# height = 0(모두 전체 보여줌), 3(리스트 3개만 보여줌)
listbox = Listbox(root, selectmode="extended", height=0) # 목록 위젯 생성
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # 리스트 박스 맨 끝에 추가할 경우 그냥 ENC로 표시해도 됨
listbox.insert(END, "포도")
listbox.pack()


# 버튼 생성
def btncmd():
    # 목록 삭제
    # listbox.delete(END) # 맨 뒤에 목록 삭제
    # listbox.delete(0) # 맨 앞에 목록 삭제

    # 개수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 목록 확인
    get_list = listbox.get(0, 2) # 0(1번) ~ 2(3번)까지
    print("1번째 ~ 3번째 까지의 목록 : {0}".format(get_list)) 

    # 선택 목록 확인
    selected_list = listbox.curselection()
    print("선택된 목록 : {0}".format(selected_list)) # index 값으로 출력

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()