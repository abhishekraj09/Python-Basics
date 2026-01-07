def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_person(name="Ram",age=30,dept="cse")
info_person(name="shyam",dept="ece")    