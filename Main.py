from Print_All_Students import PrinAllStudents
from SearchStudent import searchStudent
from Main_Menu import MainMenu
from Student import StudentInfo
from Add_Student import AddStudent

stu = StudentInfo()
printAll = PrinAllStudents(stu.allstudents) 
addStu = AddStudent(stu)
srch = searchStudent(stu)

menu = MainMenu(addStu, srch, printAll)

attempts = 0

print("⤇"*10, "Student Information System", "⤆"*10)
while attempts < 4:
    
    login_check = input("Enter student ID: ").strip()
    user = srch.verify_login(login_check)
    if user != False or login_check == "admin":
        menu.main_menu(user)
        break
    else:
        attempts += 1
        print("Invalid Login\n")

    if attempts > 3:
        print("You have reached the maximum attempts")
