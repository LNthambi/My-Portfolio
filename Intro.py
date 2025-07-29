#PLP = "Academy" 

Student_Name = "Lynne Nthambi"

Student_ID = 1001

Student_Age = 20.2

Fees_Clearance = True

print(Student_Name, Student_ID, Student_Age, Fees_Clearance)

print(f"Welcome to PLP Academy {Student_Name}. Your ID is {Student_ID} and you are {Student_Age} years old. Fees clearance status: {Fees_Clearance}.")


#Lists

Languages = ["Python", "Java", "C++", "JavaScript"]
print(Languages)

#Shopping List
Shopping_List = ["Apples", "Bananas", "Oranges", "Grapes"]
print(Shopping_List)
print(Shopping_List[0])  # Accessing the first item

#Tuples
products = ("Laptop", "Smartphone", "Tablet", 23, 499.99)
print(products)
print(products[0])  # Accessing the first item

#Sets
Set_A = {1, 2, 3, 4, 5}
Set_B = {4, 5, 6, 7, 8}
print(Set_A)
print(Set_B)
print(Set_A.union(Set_B))  # Union of two sets
print(Set_A.intersection(Set_B))  # Intersection of two sets

#Dictionaries
student_info = {
    "Name": "Lynne Nthambi",
    "ID": 1001,
    "Age": 20.2,
    "Fees_Clearance": True
}
print(student_info)

Capital_Cities = {
    "Kenya": "Nairobi", 
    "Uganda": "Kampala",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali"}
print(Capital_Cities)