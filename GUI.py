from tkinter import *
win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
def content1_button():
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont1_div.pack(side="left", fill="both", expand=True)
def content2_button():
    cont1_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont2_div.pack(side="left", fill="both", expand=True)
def content3_button():
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont3_div.pack(side="left", fill="both", expand=True)
def content4_button():
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont5_div.pack_forget()
    cont4_div.pack(side="left", fill="both", expand=True)
def content5_button():
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack(side="left", fill="both", expand=True)
btns = []
func = [content1_button, content2_button, content3_button, content4_button, content5_button]
btn_txt = ["View your own information","View another student's information","Register a New Student","Print all students in the list","Exit"]
main_div = Frame(win, bg="white")
main_div.pack(side="left", fill="both", expand=True)
menu_div = Frame(main_div, bg="#78909C")
menu_div.pack(side="left", fill="y")
cont1_div = Frame(main_div, bg="blue")
Label(cont1_div, width=30, text="Content 1: Your Information", font=("Century Gothic", 14), pady=15).grid(row=0, column=0)
cont2_div = Frame(main_div, bg="yellow")
Label(cont2_div, width=30, text="Content 2: Another Student's Information", font=("Century Gothic", 14), pady=15).grid(row=0, column=0)
cont3_div = Frame(main_div, bg="red")
Label(cont3_div, width=30, text="Content 3: Register a New Student", font=("Century Gothic", 14), pady=15).grid(row=0, column=0)
cont4_div = Frame(main_div, bg="white")
Label(cont4_div, width=30, text="Content 4: Print All Students", font=("Century Gothic", 14), pady=15).grid(row=0, column=0)
cont5_div = Frame(main_div, bg="black")
Label(cont5_div, width=30, text="Content 5: Exit", font=("Century Gothic", 14), pady=15, fg="black").grid(row=0, column=0)
Label(menu_div, width=20, text="Main Menu", font=("Century Gothic", 14), pady=15).grid(row=0, column=0)
for i in range(len(btn_txt)):
    btns.append(Button(menu_div, anchor="e", bg="#FFFFFF", text=btn_txt[i], width=25,
                       font=("Century Gothic", 14), padx=15))
    btns[i].grid(row=i+1, column=0)
    btns[i].config(command=func[i])
content1_button()
win.mainloop()