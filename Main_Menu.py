class MainMenu:
    def __init__(self, addStu, srch, printAll):
        self.addStu = addStu  # Instance for adding students
        self.srch = srch      # Instance for searching students
        self.printAll = printAll  # Instance for printing all students

    def main_menu(self, user):
        print(f"Welcome {user[0]}!")  # Use the user object to get the name
        while True:
            print("\nPlease select a number based on what you want to do:")
            print("1. View your own information")
            print("2. View another student's information")
            print("3. Register a New Student")
            print("4. Print all students in the list")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("⤇"*10, "User Information",  "⤆"*10)
                print("")
                print(f"Name: {user[0]}\nID: {user[1]}\nAge: {user[2]}\nEmail: {user[3]}\nPhone: {user[4]}\n")  
                print("⤇"*10, "Nothing Follows",  "⤆"*11)

            elif choice == 2:
                student_id = input("Enter the Student ID: ")
                self.srch.find_student(student_id)
                

            elif choice == 3:
                self.addStu.add_student_input()  
            elif choice == 4:
                self.printAll.print_allstudents() 

            elif choice == 5:
                print("Program Shutdown Successfully")
                break

            else:
                print("Invalid choice, please try again.")