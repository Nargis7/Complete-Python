# def decorator(func):
#     def wrapper(a,b):
#         print("THE ADDITION OF TWO NUMBERS ARE:")

#         func(a,b)

#         print("THANK YOU!") 

#     return wrapper       


# @decorator
# def addition(a,b):
#     print(f"Your total number is: {a+b}")


# addition(10,30)



def decorator(func):
    def wrapper(*args, **kwargs):
        print("THE ADDITION OF TWO NUMBERS ARE:")

        func(*args, **kwargs)

        print("THANK YOU!") 

    return wrapper       


@decorator
def addition(a,b):
    print(f"Your total number is: {a+b}")


addition(10,30) 

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum +=i

#     print(sum)    


# addition(12,34,56,78,666,743,246,322,23,45,56)




def addition(**kwargs):
    print(kwargs)
        


addition(a=37,b=45,c=78)




