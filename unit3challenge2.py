def _init_(self, name, roll_number, cgpa):
  self.name = name
  self.roll_number = roll_number
  self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students

students = [
    Student("Abishek", "701", 8.8),
    Student("Anu", "702", 9.7),
    Student("Sreedhar", "703", 8.2),
    Student("Manish", "704", 7.9),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: ",student.name,", Roll Number: ",student.roll_number," CGPA: ",student.cgpa)