from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480+300+100")

def create_new_file():
    print("새로운 파일을 만듭니다.")

# File Menu
menu = Menu(root)
menu_file = Menu(menu, tearoff=0) # root가 아닌 menu에 넣음
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disabled") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # root 창 닫기

menu.add_cascade(label="File", menu=menu_file) # File이라는 menu에 menu_file들 들어감

# Edit Menu (빈 값)
menu.add_cascade(label="Edit")

# Language Menu Add (라디오 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View Menu add CheckBox Menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu) # root에 menu 추가
root.mainloop()