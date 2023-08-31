class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa
        
    def __str__(self):
        return f"Student name: {self.name}\nStudent ID: {self.school_id}\nGPA: {self.gpa}"

alex = Student("alex", "1", 3)
sam = Student("sam", "2", 6)
print(alex, sam, sep="\n")