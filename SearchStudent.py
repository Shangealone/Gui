class searchStudent:
    def __init__(self, student_info):
        self.student_info = student_info.allstudents  

    def verify_login(self, id_number):
        id_number = id_number.strip()  # Remove any whitespace
        
        for student in self.student_info:
            if student[2].strip() == id_number:  
                return student  # Return the student record if found
        
        return False
    
    def find_student(self, id_number):
        id_number = id_number.strip()  
        print("")
        print("⤇"*10, "Finding Student", "⤆"*10)
        for student in self.student_info:
            if student[2].strip() == id_number:
                print(f"Name: {student[0]}\nAge: {student[1]}\nID: {student[2]}\nEmail: {student[3]}\nNumber: {student[4]}") 
        print("⤇"*11, "Student Found", "⤆"*11)
        return False
        

