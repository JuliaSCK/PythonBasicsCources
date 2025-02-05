student = {
    "name": "John Smith",
    "age": 25,
    "course": "Computer Science"
}

print(student)
print(type(student))
print("Age: " , student["age"])
print("Name: " , student["name"])
print("Course: " , student["course"])

print("-*-*-*-*-*-*-*-*-*-*-*-")
# Ex. 3
students = {
    "student_1": {
        "Name": "Alla",
        "Age": 85
    },
    "student_2": {
        "Name": "Anna",
        "Age": 35
    },
    "student_3": {
        "Name": "Maria",
        "Age": 37
    },
    "student_4": {
        "Name": "Villi",
        "Age": 36
    },
    "student_5": {
        "Name": "Nata",
        "Age": 49
    }
}
print(students["student_3"])
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# Access the nested dictionary for "student_5"
student_5_info = students["student_5"]
# Extract the "Name" from the nested dictionary
name_of_student_5 = student_5_info["Name"]
print(name_of_student_5)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
# Unpack the nested dictionary directly
name_of_student_4, age_of_student_4 = students["student_4"].values()
print(name_of_student_4)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
name_of_student_2 = students["student_2"]["Name"]
print(name_of_student_2)

