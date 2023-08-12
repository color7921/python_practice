class Student:
    def __init__(self, name, id, year, major, score):
        self.name = name
        self.id = id
        self.year = year
        self.major = major
        self.score = score

    def get_info(self):
        return f"이름:{self.name}, 학번:{self.id}, 학년:{self.year}, 전공:{self.major}, 성적:{self.score}"

class StudentManager:
    def __init__(self):
        self.s_list= []

    def add_student(self, student):
        self.s_list.append(student)

    def show_all_students(self):
        for student in self.s_list:
            print(student.get_info())

    def remove_student(self, id):
        for student in self.s_list:
            if student.id == id:
                self.s_list.remove(student)

    def find_student(self, id):
        for student in self.s_list:
            if student.id == id:
               print(student.get_info())

    
student_M = StudentManager()

student1 = Student('홍길동', '2023001', '2', '컴퓨터공학과', 90.5)
student2 = Student('김철수', '2023002', '3', '전자공학과', 85.5)
student3 = Student('이영희', '2023003', '1', '수학', 92.8)
student_M.add_student(student1)
student_M.add_student(student2)
student_M.add_student(student3)


student_M.remove_student('2023002')

student_M.show_all_students()
print("="*30)

student_M.find_student('2023001')
print("="*30)
student_M.show_all_students()

print(student_M.s_list)