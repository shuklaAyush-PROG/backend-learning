
from database import get_all_students, get_student_by_id

students = get_all_students()
print("All students:", students)

if students:
    student_id = students[0][0]
    student = get_student_by_id(student_id)
    print("First student:", student)
else:
    print("No students found yet.")
