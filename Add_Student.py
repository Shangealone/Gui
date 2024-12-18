from tkinter import Label, Entry, Button, messagebox, Frame  # Ensure tkinter components are imported

class AddStudent:
    def __init__(self, student):
        self.student_info = student

    def add_student(self, name, age, id_number, email, phone):
        self.student_info.setName(name)
        self.student_info.setAge(age)
        self.student_info.setId_number(id_number)
        self.student_info.setEmail(email)
        self.student_info.setPhone(phone)
        stud_written = [name, age, id_number, email, phone]
        self.student_info.allstudents.append(stud_written)
        print(f"\nAdded student {stud_written[0]} to the list.")
        print("⤇" * 6, "Student Added Successfully", "⤆" * 6)
        self.write_to_file(stud_written)

    def write_to_file(self, data_to_write):
        with open("Student_List.txt", "a+") as file:
            file.write(", ".join(data_to_write) + "\n")

    def show_reg_ui(self, reg_frame):
        """Displays the registration UI in the given frame."""
        # Frame for registration form
        reg_frame.configure(bg="#FFF5EE")

        # Error Label
        self.LblErrors = Label(reg_frame, text="", font=("Arial", 16), fg="red", bg="#FFF5EE")
        self.LblErrors.grid(row=1, column=0, columnspan=4)

        # Registration Labels and Entries
        self.reg_txt = ["Name:", "Age:", "Student ID:", "Email Address:", "Phone Number:"]
        self.reg_entry = []
        
        for i in range(len(self.reg_txt)):
            # Label
            label = Label(reg_frame, text=self.reg_txt[i], font=("Arial", 16), bg="#FFF5EE")
            label.grid(row=i + 2, column=0, padx=10, pady=5, sticky="e")

            # Entry
            entry = Entry(reg_frame, width=40, font=("Arial", 16), borderwidth=2, relief="groove")
            entry.grid(row=i + 2, column=1, columnspan=3, padx=10, pady=5)
            self.reg_entry.append(entry)
        
        # Register Button
        reg_btn = Button(reg_frame, text="Register Student", font=("Arial", 16), bg="#5999bf", fg="white",
                         activebackground="#357ABD", command=self.check_entries, borderwidth=0)
        reg_btn.grid(columnspan=4, pady=20)

    def check_entries(self):
        """Validates and processes registration entries."""
        errors = []
        for i in range(len(self.reg_entry)):
            if self.reg_entry[i].get() == "":
                errors.append(f"You forgot to add the {self.reg_txt[i]}\n")
        
        if not errors:
            # Add student to the list
            self.add_student(
                self.reg_entry[0].get(),
                self.reg_entry[1].get(),
                self.reg_entry[2].get(),
                self.reg_entry[3].get(),
                self.reg_entry[4].get()
            )
            messagebox.showinfo("Register Success", "Added student to the list")
        else:
            self.LblErrors.config(text=f"The following error(s) occurred: \n{''.join(errors)}\nPlease try again.")
