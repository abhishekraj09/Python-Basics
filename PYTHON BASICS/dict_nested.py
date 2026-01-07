student_data={
    "Ram":{"roll_no": 10, "age":21, "course": "python"},
    "mohan":{"roll_no": 12, "age":22, "course": "java"}
}
print(student_data["mohan"])
print(student_data["mohan"]["roll_no"])
student_data["mohan"]["phone_no"]=8726262712
print(student_data["mohan"])
print(student_data["mohan"].pop("phone_no"))
print(student_data["mohan"])

travel_data = {
    "gujrat": ["dwarkadhish","somnath", "statue of unity"],
    "rajasthan":["jaipur", "udaipur"]
}
print(travel_data["rajasthan"])

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
        "course": "java"
    }
    ]

print(porf_data)