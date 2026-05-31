# class MyClass:
#     x = 12 # attributes

#     def hello(self): #method
#         print("Hello")
#     print("How are you!")

# # MyClass()
# # print(MyClass().x) 
# # MyClass().hello()       

# # object
# p1 = MyClass()
# p2 = MyClass()

# print(p1.x)
# print(p2.x)



# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets=pockets

#     def display(self):
#         print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

# p1 =Factory("leather",3,2) 
# p2 =Factory("denim",2,4)
# p3 =Factory("canvas",1,3)
# p1.display()
# p2.display()
# p3.display()

# print(p2.zips)
# print(p3.pockets)


class Animal:
    name = "Lion" # class attribute

    def __init__(self,age):
        self.age=age #instance attributes

    def show(self):
        print("how r u")

    @classmethod
    def hello(cls):
        print("Heyyyyy")  

    @staticmethod
    def bye():
        print("Goodbye")


obj = Animal(5)

obj.show() # instance method
Animal.hello() # class method
Animal.bye() # static method
