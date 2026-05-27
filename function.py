# def greet():
#     print("Hello welcome to python")

# greet()    

def greet(name):
    print(f"Hello my name is {name}")


greet("Nargis")    

def add(a,b):
    return a + b
print(add(2,2))

def introduce(name, age):
    print(f"my name is {name} and age is {age}")

introduce("Nargis", 21)    

def introduce1(name= "nargis"):
    print(f"my name is {name}")

introduce1()    
introduce1("suraj")