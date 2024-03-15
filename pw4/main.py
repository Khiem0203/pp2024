import input

students = []
courses = []
marks = []

def main():                   
    print("List of students: ")
    for student in students:
        print(student)
    
    print("List of courses: ")
    for course in courses:
        print(course)
        
    print("Student's marks: ")
    for course in courses:
        for student_mark in course.getStudent_in_course():
            print(student_mark)
    
    students.sort(key=lambda x: x.calculate_GPA(), reverse=True)
    print("\nStudents sorted by GPA:")
    for student in students:
        print(student)

main()