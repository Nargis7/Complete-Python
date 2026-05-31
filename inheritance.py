# #inheritance
# class A:
#     def method1(self):
#         print("This is method 1 of class A")
#         return "Method 1 result"

# class B(A):
#     def method2(self):
#         print("This is method 2 of class B")
#         return "Method 2 result"

# # Creating objects of both classes
# obj_a = A()
# obj_b = B()

# # Calling methods
# print(obj_a.method1())  # Calls method from class A
# print(obj_b.method1())  # Calls method from class A (inherited)
# print(obj_b.method2())  # Calls method from class B

#constructor
class Person:
    def __init__(self, name):
        self.name = name
       

    def display(self):
        print(f"Name: {self.name}")


class Employee(Person):
       
    def __init__(self, name, age):
            super().__init__(name)  # Call the constructor of the parent class
            self.age = age

    def display(self):
            print(f"Name: {self.name}, Age: {self.age}")  

p1 = Person("Alice")
e1 = Employee("Bob", 25)
p1.display()  # Calls method from class Person
e1.display()  # Calls method from class Employee


# multilevel inheritance