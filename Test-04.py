from tkinter import *
from tkinter import messagebox
from Print_All_Students import PrinAllStudents
from SearchStudent import searchStudent
from Student import StudentInfo
from Add_Student import AddStudent
from functools import partial

# Initialize main objects
win = Tk()
win.geometry("1280x800+{}+{}".format((win.winfo_screenwidth()-1280)//2, (win.winfo_screenheight()-800)//2))
win.title("Student Information System")

btn_txt = ["MyInfo", "Search Student", "Add Student", "View All Students", "Logout"]
stu = StudentInfo()
addstud = AddStudent(stu)
search = searchStudent(stu)
printAll = PrinAllStudents(stu)
current_user = None

# Function Definitions
def login_confirm():
    global current_user
    student_id = login_entry.get().strip()
    current_user = search.verify_login(student_id)
    messagebox.showinfo("Login", f"Welcome {current_user[0]}!") if current_user else messagebox.showerror("Login Failed", "Invalid Student ID.")
    login_frame.pack_forget() if current_user else None
    main_frame.pack(fill="both", expand=True) if current_user else None
    show_myinfo()

def logout_confirm():
    global current_user
    current_user = None
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, close):
    for frame in close: frame.pack_forget()
    frame_open.pack(side="right", fill="both", expand=True)

def show_myinfo():
    myinfo_label.config(text=f"Name: {current_user[0]}\nAge: {current_user[1]}\nID: {current_user[2]}\nEmail: {current_user[3]}\nPhone: {current_user[4]}") if current_user else myinfo_label.config(text="No user is logged in.")

def search_student():
    def perform_search():
        student = search.verify_login(search_entry.get().strip())
        search_result_label.config(text=f"Name: {student[0]}\nAge: {student[1]}\nID: {student[2]}\nEmail: {student[3]}\nPhone: {student[4]}") if student else search_result_label.config(text="Student not found.")
    for widget in container[1].winfo_children(): widget.destroy()
    Label(container[1], text="Enter Student ID:", font=("Tahoma", 20, "italic"), bg="pink").pack(pady=10)
    search_entry = Entry(container[1], width=30, font=("Tahoma", 20)); search_entry.pack(pady=10)
    Button(container[1], text="Search", font=("Tahoma", 20), command=perform_search).pack(pady=10)
    search_result_label = Label(container[1], text="", font=("Tahoma", 20), bg="pink"); search_result_label.pack(pady=20)

# Frames
login_frame = Frame(win, bg="black")
login_frame.pack(fill="both", expand=True)
login_form = Frame(login_frame, bg="white", padx=20, pady=20); login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Login", font=("Tahoma", 20, "bold"), bg="white").pack()
Label(login_form, text="Enter Student ID:", font=("Tahoma", 16), bg="white").pack(pady=10)
login_entry = Entry(login_form, font=("Tahoma", 16)); login_entry.pack(pady=10)
Button(login_form, text="Login", bg="skyblue", font=("Tahoma", 16), command=login_confirm).pack(pady=10)
Button(login_form, text="Exit", bg="skyblue", font=("Tahoma", 16), command=win.destroy).pack(pady=10)

main_frame = Frame(win, bg="#57586C")
menu_contain = Frame(main_frame, borderwidth=0, bg="black"); menu_contain.pack(side="left", fill="y")
content_frame = Frame(main_frame, borderwidth=0, bg="#57586C"); content_frame.pack(side="right", fill="both", expand=True)
container = [Frame(content_frame, bg="pink") for _ in btn_txt]; [frame.pack_forget() for frame in container]

# MyInfo Frame
myinfo_label = Label(container[0], text="", font=("Tahoma", 20), bg="pink", justify=LEFT); myinfo_label.pack(pady=20)

# Add Buttons to Menu
func = [partial(open_frame, container[0], container[1:]), partial(open_frame, container[1], container[:1] + container[2:]), partial(open_frame, container[2], container[:2] + container[3:]), partial(open_frame, container[3], container[:3] + container[4:]), logout_confirm]
for i in range(len(btn_txt)):
    Button(menu_contain, text=btn_txt[i], bg="skyblue", font=("Tahoma", 20), width=20, command=func[i]).pack(pady=5)

# Add Student UI
addstud.show_reg_ui(container[2])

# View All Students Frame
view_all_label = Label(container[3], text="All Students", font=("Tahoma", 20, "bold"), bg="pink"); view_all_label.pack()
def show_all_students():
    result_text = "\n".join([f"Name: {s[0]}, Age: {s[1]}, ID: {s[2]}, Email: {s[3]}, Phone: {s[4]}" for s in stu.allstudents])
    Label(container[3], text=result_text, font=("Tahoma", 16), bg="pink", justify=LEFT).pack(pady=10)
show_all_students()
search_student()

win.mainloop()
