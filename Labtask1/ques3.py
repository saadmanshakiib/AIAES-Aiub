products = ["Phone","Laptop","PC"]
print(products)
products.append("TV")
print(products)
products.remove("PC")
print(products)

student = {
        "name" : "Sadman",
        "age" : 23,
        "department" : "CSE"
    }
print(student)
student["cgpa"] = 3.40
print(student)
student.pop("department")
print(student)