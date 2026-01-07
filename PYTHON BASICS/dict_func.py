porf_data=[

    {  
        "name": "Ram",
        "roll_no": 10, 
        "age":21, 
        "course": "python"
    },

    {

    "name":"mohan",
        "roll_no": 12,
        "age":22, 
        "course": "java",
    }
]

def add_new_student(name, rollno, age,course_opted):
    new_student = {}
    new_student["Name"] = name
    new_student["roll_no"] = rollno
    new_student["age"] = age
    new_student["course"] = course_opted
    porf_data.append(new_student)

add_new_function =("shyam",22,18,"c++")
print(porf_data)