# student_list=[]
# student1={"name":"nusu","id":11,"maths":89,"science":78,"english":99}
# student2={"name":"nida","id":22,"maths":85,"science":67,"english":34}
# student3={"name":"fida","id":33,"maths":34,"science":47,"english":98}
# student_list={"student1":student1,"student2":student2,"student3":student3}
# # student_list.append(student1)
# # student_list.append(student2)
# # student_list.append(student3)
# print(student_list)
# total_s1=student1.get(maths)

def calculate_average_score(student):
    math_score = student["Math"]
    science_score = student["Science"]
    english_score = student["English"]
    average_score = (math_score + science_score + english_score) / 3
    return average_score

student_list = []

student1 = {
    "Name": "John Smith",
    "Student ID": 101,
    "Math": 90,
    "Science": 85,
    "English": 88
}
student1["Average"] = calculate_average_score(student1)
student_list.append(student1)

student2 = {
    "Name": "Jane Doe",
    "Student ID": 102,
    "Math": 78,
    "Science": 92,
    "English": 86
}
student2["Average"] = calculate_average_score(student2)
student_list.append(student2)

student3 = {
    "Name": "Bob Johnson",
    "Student ID": 103,
    "Math": 85,
    "Science": 75,
    "English": 90
}
student3["Average"] = calculate_average_score(student3)
student_list.append(student3)

print("Student Report:")
for student in student_list:
    print(f"Name: {student['Name']}")
    print(f"Student ID: {student['Student ID']}")
    print(f"Math Score: {student['Math']}")
    print(f"Science Score: {student['Science']}")
    print(f"English Score: {student['English']}")
    print(f"Average Score: {student['Average']:.2f}\n")
