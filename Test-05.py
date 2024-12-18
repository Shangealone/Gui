from tkinter import *
from tkinter import messagebox
from functools import partial
from Print_All_Students import PrinAllStudents
from SearchStudent import searchStudent
from Student import StudentInfo
from Add_Student import AddStudent

# Basic window setup
win = Tk()
win.geometry("1280x800+{}+{}".format((win.winfo_screenwidth()-1280)//2, (win.winfo_screenheight()-800)//2))
win.title("Student Information System")
win.configure(bg="#0a1324")

# Initialize dependencies
stu = StudentInfo()
addstud = AddStudent(stu)
search = searchStudent(stu)
current_user = None
login_attempts = 0  # Counter for login attempts

# ================== Reusable Styling ======================

def styled_label(parent, text, font_size=14, color="#555", **kwargs):
    return Label(parent, text=text, font=("Arial", font_size, 'bold'), bg="#FFF5EE", fg=color, **kwargs)

def styled_button(parent, text, command):
    button = Button(parent, text=text, font=("Arial", 14), bg="#4A90E2", fg="white", activebackground="#357ABD", borderwidth=0, command=command)
    button.bind("<Enter>", lambda e: button.config(bg="#357ABD"))  # Hover effect
    button.bind("<Leave>", lambda e: button.config(bg="#4A90E2"))
    return button

def create_rounded_frame(parent, bg_color="#FFF5EE"):
    frame = Frame(parent, bg=bg_color, highlightbackground="#ccc", highlightthickness=1, padx=20, pady=20)
    frame.config(relief="groove", bd=2)
    return frame

# ================== Functions ===================

def login_confirm():
    global current_user, login_attempts
    student_id = login_entry.get().strip()
    current_user = search.verify_login(student_id)

    if current_user:
        messagebox.showinfo("Login", f"Welcome {current_user[0]}!")
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        show_myinfo()
        login_attempts = 0  # Reset attempts on successful login
    else:
        login_attempts += 1
        messagebox.showerror("Login Failed", f"Invalid Student ID. Attempt {login_attempts}/4.")
        
        # Disable the login button after 4 attempts
        if login_attempts >= 4:
            login_entry.config(state='disabled')
            login_btn.config(state='disabled')
            messagebox.showerror("Max Attempts", "You have exceeded the maximum number of login attempts.")

def logout_confirm():
    global current_user
    current_user = None
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)
    reset_login()  # Reset login attempts on logout

def reset_login():
    global login_attempts
    login_attempts = 0
    login_entry.config(state='normal')  # Enable the login entry
    login_btn.config(state='normal')  # Enable the login button

def open_frame(frame_open, close):
    for frame in close: 
        frame.pack_forget()
    frame_open.pack(side="right", fill="both", expand=True)

def show_myinfo():
    if current_user:
        info_text = f"Name: {current_user[0]}\nAge: {current_user[1]}\nID: {current_user[2]}\nEmail: {current_user[3]}\nPhone: {current_user[4]}"
    else:
        info_text = "No user is logged in."
    myinfo_label.config(text=info_text)

def search_student():
    for widget in container[1].winfo_children(): 
        widget.destroy()

    styled_label(container[1], "Search Student", 18, color="#0a1324").pack(pady=10)
    styled_label(container[1], "Enter Student ID:", 14).pack(pady=5)
    search_entry = Entry(container[1], font=("Arial", 14), width=30, borderwidth=2, relief="groove")
    search_entry.pack(pady=5)

    def perform_search():
        student = search.verify_login(search_entry.get().strip())
        if student:
            result_text = f"Name: {student[0]}\nAge: {student[1]}\nID: {student[2]}\nEmail: {student[3]}\nPhone: {student[4]}"
        else:
            result_text = "Student not found."
        search_result_label.config(text=result_text)

    styled_button(container[1], "Search", perform_search).pack(pady=10)
    search_result_label = styled_label(container[1], "", 14)
    search_result_label.pack(pady=20)

def view_all_students():
    for widget in container[3].winfo_children(): 
        widget.destroy()

    styled_label(container[3], "All Students", 18, color="#0a1324").pack(pady=10)

    # Create a canvas and a scrollbar
    canvas = Canvas(container[3], bg="#FFF5EE")
    scrollbar = Scrollbar(container[3], orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#FFF5EE")

    # Configure the scrollbar
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a window in the canvas to hold the scrollable frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure canvas scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Table headers
    headers = ["Name", "Age", "ID", "Email", "Phone"]
    for col, header in enumerate(headers):
        styled_label(scrollable_frame, header, 14, "#4A90E2").grid(row=0, column=col, padx=10, pady=5, sticky="w")

    # Populate the scrollable frame with student data
    for idx, student in enumerate(stu.allstudents, start=1):
        for col, value in enumerate(student):
            styled_label(scrollable_frame, value, 12).grid(row=idx, column=col, padx=10, pady=5, sticky="w")

    # Frame for the refresh button
    refresh_frame = Frame(container[3], bg="#FFF5EE")
    refresh_frame.pack(side="bottom", fill="x", pady=10)

    # Refresh button
    styled_button(refresh_frame, "Refresh", view_all_students).pack()

# ================== Frames Setup ====================

# Login Frame
login_frame = Frame(win, bg="#FFF5EE")
login_frame.pack(fill="both", expand=True)

login_form = create_rounded_frame(login_frame)
login_form.place(relx=0.5, rely=0.5, anchor="center")

styled_label(login_form, "Login", 20, color="#0a1324").pack(pady=10)
styled_label(login_form, "Enter Student ID:", 14).pack(pady=5)
login_entry = Entry(login_form, font=("Arial", 14), width=30, borderwidth=2, relief="groove")
login_entry.pack(pady=5)

login_btn = styled_button(login_form, "Login", login_confirm)
login_btn.pack(pady=5)
styled_button(login_form, "Exit", win.destroy).pack(pady=5)

# Main Frame
main_frame = Frame(win, bg="#0a1324")
container = [create_rounded_frame(main_frame) for _ in range(5)]
for frame in container: 
    frame.pack_forget()

myinfo_label = styled_label(container[0], "", 14)
myinfo_label.pack(expand=True)

func = [
    partial(open_frame, container[0], container[1:]),
    partial(open_frame, container[1], container[:1] + container[2:]),
    partial(open_frame, container[2], container[:2] + container[3:]),
    partial(open_frame, container[3], container[:3] + container[4:]),
    logout_confirm
]

# Sidebar
menu_contain = Frame(main_frame, bg="#3a4754")
menu_contain.pack(side="left", fill="y")

btn_txt = ["MyInfo", "Search Student", "Add Student", "View All Students", "Logout"]
# Update styled_button to accept a width parameter
def styled_button(parent, text, command, width=20):  # Set a default width
    button = Button(parent, text=text, font=("Arial", 14), bg="#4A90E2", fg="white",
                    activebackground="#357ABD", borderwidth=0, command=command, width=width)
    button.bind("<Enter>", lambda e: button.config(bg="#357ABD"))  # Hover effect
    button.bind("<Leave>", lambda e: button.config(bg="#4A90E2"))
    return button

# New button texts and corresponding functions
btn_txt = ["My Information", "Find Student", "Register New Student", "List All Students", "Logout"]
func = [
    partial(open_frame, container[0], container[1:]),  # My Information
    partial(open_frame, container[1], container[:1] + container[2:]),  # Find Student
    partial(open_frame, container[2], container[:2] + container[3:]),  # Register New Student
    partial(open_frame, container[3], container[:3] + container[4:]),  # List All Students
    logout_confirm  # Logout
]

# Create buttons in the sidebar with a consistent width
button_width = 20  # Set the desired button width
for text, function in zip(btn_txt, func):
    styled_button(menu_contain, text, function, width=button_width).pack(pady=5)

# Initialize Add and View Students UI
addstud.show_reg_ui(container[2])
view_all_students()
search_student()

# ================= Main Loop ======================

win.mainloop()
