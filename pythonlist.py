grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)
average_grade = sum(grades) / len(grades)
print(average_grade)
grades[7] = "failed"
grades[8] = "failed"
grades[9] = "failed"
print(grades)


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
did_both = [student for student in submitted if student in attended]
print(did_both)
list_equal = [len(submitted) == len(attended)]
print(list_equal)
attended.remove("Eve")
attended.remove("Frank")
print(attended) 


temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]
print(second_week)
temp_over_100 = [temp for temp in temperatures if temp > 100]
print(temp_over_100)
temperatures.reverse()
print(temperatures)
fifth_to_tenth_day = temperatures[5:10]
print(fifth_to_tenth_day)

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
for i in range(len(students)):               
    if grades[i] < 80:
        print("name of student", students[i], "grade", grades[i], "activity", activities[i])
students_approved = ["john", "Doe", "Smith"]
print(students_approved)

   


