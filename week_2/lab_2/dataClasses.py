from dataclasses import dataclass
@dataclass 

# I like this better because it's cleaner and I don't need a use __ init __ methods

class Student: # student class that represents a student object that contains the name, college id, and gpa
  name: str 
  college_id: int
  gpa: float
  
def main():
    students = add_student() # add student to list
    for s in students:
        show_student(s) # print student info
            

def add_student():
    students =[] # list of students
    while True:
        
        if input("Do you want to a student? (y/n): ") == "n": # if user enters n, break out of loop
            break
        else:
            S_name = input("Enter student name: ")
            S_id = int(input("Enter student ID: "))
            S_gpa = float(input("Enter student GPA: "))
            S = Student(S_name, S_id, S_gpa) # add student object to list
            students.append(S)
            
    return students # return list of students
            
        
    
def show_student(S):
    print(f"Student name: {S.name}")
    print(f"Student ID: {S.college_id}")
    print(f"Student GPA: {S.gpa}")


            
main ()


