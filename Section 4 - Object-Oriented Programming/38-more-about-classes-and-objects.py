class Student:
  def __init__(self, new_name, new_grade):
    self.name = new_name
    self.grades = new_grade

  def average(self):
    return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)

# This outputs the same thing
print(student_one.average())
print(Student.average(student_one))

# This outputs the same thing
print(student_two.average())
print(Student.average(student_two))