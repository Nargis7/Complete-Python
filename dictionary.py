student = {
    "name": "Nargis",
    "age": 20,
    "course": "Python"
}

# print(student["name"]) # Nargis
# print(student.get("age")) # 20
# print(student.get("course")) # Python

# # adding new key-value pair
student["grade"] = "A"
# print(student.get("grade")) # A

# # updating value of existing key
# student["age"] = 21
# print(student.get("age")) # 21

# # removing key-value pair
# student.pop("grade")
# print(student.get("grade")) # None
# del student["course"]
# print(student.get("course")) # None


# iterating through dictionary
# for key, value in student.items():
#     print(f"{key}: {value}")

# help(dict)

# deep copy -> creates a new object and recursively copies all the objects found in the original object. It is used when you want to create a completely independent copy of an object, including all nested objects.
a = [1,2,3,4,5]

b = a.copy()
b[0] = 10
print(a)
 # [1, 2, 3, 4, 5]
print(b)
# [10, 2, 3, 4, 5] 

# shallow copy -> creates a new object but does not create copies of nested objects. Instead, it references the same nested objects as the original. It is used when you want to create a new object that shares some of the same data as the original, but you don't need to modify the nested objects independently.
a = [1,2,3,4,5]
b = a
b[0] = 10
print(a) # [10, 2, 3, 4, 5]
print(b) # [10, 2, 3, 4, 5]