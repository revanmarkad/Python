# Define the gradingStudents function
def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            mod = grade % 5
            if mod >= 3:
                grade += (5 - mod)
        rounded_grades.append(grade)
    return rounded_grades

 
grades = [73, 67, 38, 33]
rounded_grades = gradingStudents(grades)
print(rounded_grades)
