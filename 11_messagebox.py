from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

# message box eroor 가 났을 때 보여 주는 박스

# 기차 예매 시스템 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # title, content

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def ok_cancel():
    msgbox.askokcancel("확인/취소", "해당 죄석은 유아동반석입니다. 예매하시겠습니까?") # 확인 취소 사용자 선택

def retry_cancel():
    msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다. 다시 시도허시겠습니가?") # 다시 시도 사용자 선택

def yes_no():
    msgbox.askyesno("예/아니요", "해당 좌석은 역방향입니다. 예매하시겠습니까?") # 예 아니요 사용자 선택

def yes_no_cancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 하시겠습니까?") # 예 아니요 취소 사용자 선택

    # yes : 저장 후 종료
    # no : 저장하지 않고 종료
    # cancel : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("response: {0}".format(response)) # True, False, None -> 1(True), 0(False), 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    else:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=ok_cancel, text="확인 취소").pack()
Button(root, command=retry_cancel, text="재시도 취소").pack()
Button(root, command=yes_no, text="예 아니요").pack()
Button(root, command=yes_no_cancel, text="예 아니요 취소").pack()

root.mainloop()