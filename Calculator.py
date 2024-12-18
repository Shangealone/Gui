from tkinter import *
from functools import partial
win = Tk()
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "÷"]
row_num, col_num = 1, 0
res = Label(win, width=20, text="0", fg="black", bg="#c0d6e4", font=("Century Gothic", 20))
res.grid(row=0, column=0, columnspan=4)
def calculate(num):
    txt = res.cget("text")
    if num == "C":
        res.config(text="0")
    elif num == "=":
        try:
            expression = txt.replace("÷", "/")
            result = eval(expression)
            res.config(text=str(result))
        except:
            res.config(text="Error")
    else:
        res.config(text=(txt + num) if txt != "0" else num)
for txt in btn_txt:
    Button(
        win, 
        text=txt, 
        width=6, 
        bg="#c0d6e4", 
        font=("Century Gothic", 25), 
        command=partial(calculate, txt)
    ).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num == 4:
        col_num, row_num = 0, row_num + 1
win.title("Calculator")
win.config(bg="#c0d6e4")
win.geometry("647x373+500+210")
win.mainloop()