from tkinter import *
from tkinter import messagebox
from Print_All_Students import PrinAllStudents
from SearchStudent import searchStudent
from Student import StudentInfo
from Add_Student import AddStudent
from functools import partial
win = Tk()
win.geometry("1280x800+{}+{}".format((win.winfo_screenwidth()-1280)//2, (win.winfo_screenheight()-800)//2))
win.title("Student Information System")
win.configure(bg="#0a1324")
btn_txt = ["MyInfo", "Search Student", "Add Student", "View All Students", "Logout"]
stu = StudentInfo()
addstud = AddStudent(stu)
search = searchStudent(stu)
current_user = None
def login_confirm():
    global current_user
    student_id = login_entry.get().strip()
    current_user = search.verify_login(student_id)
    if current_user:
        messagebox.showinfo("Login", f"Welcome {current_user[0]}!")
        login_frame.pack_forget()  # Hide login frame
        main_frame.pack(fill="both", expand=True)  # Show main frame
        show_myinfo()
    else:
        messagebox.showerror("Login Failed", "Invalid Student ID.")
def logout_confirm():
    global current_user
    current_user = None
    main_frame.pack_forget()  # Hide main frame
    login_frame.pack(fill="both", expand=True)  # Show login frame
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
    Label(container[1], text="Enter Student ID:", font=("Arial", 16), bg="#FFF5EE").pack(pady=10)
    search_entry = Entry(container[1], font=("Arial", 16), width=30); search_entry.pack(pady=10)
    Button(container[1], text="Search", font=("Arial", 16), command=perform_search).pack(pady=10)
    search_result_label = Label(container[1], text="", font=("Arial", 16), bg="#FFF5EE"); search_result_label.pack(pady=20)
login_frame = Frame(win, bg="#FFF5EE"); login_frame.pack(fill="both", expand=True)
login_form = Frame(login_frame, bg="#FFF5EE", padx=20, pady=20); login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Login", font=("Arial", 20), bg="#FFF5EE").pack()
Label(login_form, text="Enter Student ID:", font=("Arial", 16), bg="#FFF5EE").pack(pady=10)
login_entry = Entry(login_form, font=("Arial", 16)); login_entry.pack(pady=10)
Button(login_form, text="Login", bg="#5999bf", font=("Arial", 16), command=login_confirm).pack(pady=10)
Button(login_form, text="Exit", bg="#5999bf", font=("Arial", 16), command=win.destroy).pack(pady=10)
main_frame = Frame(win, bg="#0a1324")  # Main frame for after login
container = [Frame(main_frame, bg="#FFF5EE") for _ in btn_txt]  # Container for each section
[frame.pack_forget() for frame in container]  # Initially hide all containers
myinfo_label = Label(container[0], text="", font=("Arial", 16), bg="#FFF5EE"); myinfo_label.pack(pady=20)
func = [
    partial(open_frame, container[0], container[1:]), 
    partial(open_frame, container[1], container[:1] + container[2:]), 
    partial(open_frame, container[2], container[:2] + container[3:]), 
    partial(open_frame, container[3], container[:3] + container[4:]), 
    logout_confirm
]
menu_contain = Frame(main_frame, bg="black"); menu_contain.pack(side="left", fill="y")  # Menu container
for i in range(len(btn_txt)):
    Button(menu_contain, text=btn_txt[i], bg="#5999bf", font=("Arial", 16), width=20, command=func[i]).pack(pady=5)
addstud.show_reg_ui(container[2])
Label(container[3], text="All Students", font=("Arial", 20), bg="#FFF5EE").pack()
def show_all_students():
    result_text = "\n".join([f"Name: {s[0]}, Age: {s[1]}, ID: {s[2]}, Email: {s[3]}, Phone: {s[4]}" for s in stu.allstudents])
    Label(container[3], text=result_text, font=("Arial", 16), bg="#FFF5EE", justify=LEFT).pack(pady=10)
show_all_students()
search_student()
win.mainloop()
