# class Student:
#     def __init__(self,name):
#         self.name = name

# s = Student("Nargis")
# print(s)      

# class Student:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f"Student name: {self.name}"     

# s = Student("Nargis")
# print(s)    


class Number:
    def __init__(self,pages):
        self.pages = pages


    def __add__(self, other):
         return self.pages + other.pages

n1 = Number(10)
n2 = Number(20)
print(n1+n2)       