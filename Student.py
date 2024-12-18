import time
class StudentInfo:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.id_number = ""
        self.email = ""
        self.phone = ""
        self.allstudents = []
        self.read_file()

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setId_number(self, id_number):
        self.id_number = id_number
    
    def getId_number(self):
        return self.id_number
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getPhone(self):
        return self.phone
    
    
    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nId Number: {self.id_number}\nEmail: {self.email}\nPhone: {self.phone}"

    def read_file(self):
        try:
            with open("Student_List.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:  
                        student_data = line.split(",")
                        self.allstudents.append(student_data)
        except FileNotFoundError:
            print("No student data found")