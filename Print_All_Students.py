class PrinAllStudents:
    def __init__(self, all_students):
        self.all_students = all_students  

    def studentInfo(self, student):
        self.all_students.append(student) 

    def print_allstudents(self):
        print("⤇" * 10, "All Students","⤆" * 10)
        for student in self.all_students:
            print("⤇" * 8, "Student Info","⤆" * 8)
            print("")
            print(f"Name: {student[0]}\nID: {student[1]}\nAge: {student[2]}\nEmail: {student[3]}\nPhone: {student[4]}\n")
        print("⤇" * 7, "Nothing Follows","⤆" * 6)

