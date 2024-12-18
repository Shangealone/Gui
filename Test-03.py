from tkinter import *
from functools import partial

win = Tk()
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "÷"]
row_num = 0
col_num = 0
res = Label(win, width=20, text="Very Human Calculator", fg="black", font=("Century Gothic", 20))
res.grid(row=0, column=0, columnspan=4)
equal_pressed = False
entered_first_number = False  # To track if the first number is entered

def calculate(num):
    global equal_pressed, entered_first_number
    current_text = res.cget("text")  # Get the current text displayed in the label

    if num == "=":
        # Evaluate the current expression and display the result
        try:
            expression = txt.replace("÷","/")
            result = eval(current_text)
            res.config(text=str(result))  # Show the result as a string
            equal_pressed = True
        except:
            res.config(text="Error")  # Show error if there's a mistake in the expression
            equal_pressed = True
    elif num == "C":
        # Reset to the initial state
        res.config(text="Very Human Calculator")
        equal_pressed = False
        entered_first_number = False
    else:
        if equal_pressed:
            # After pressing equals, replace the result with the new input
            res.config(text=num)
            equal_pressed = False
            entered_first_number = True
        else:
            if not entered_first_number:
                # Replace "Very Human Calculator" with the first number pressed
                res.config(text=num)
                entered_first_number = True
            else:
                # Append the number to the current text
                res.config(text=current_text + num)

# Create buttons
for i in range(len(btn_txt)):
    Button(win, width=8, text=btn_txt[i], bg="#c0d6e4", font=("Century Gothic", 25), command=partial(calculate, btn_txt[i])).grid(row=row_num + 2, column=col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0

win.title("Calculator")
win.config(bg="#c0d6e4")
win.geometry("647x373+500+210")
win.mainloop()