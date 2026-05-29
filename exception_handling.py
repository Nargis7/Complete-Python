# a = int(input("Enter number: "))

# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Sorry you cannot divide by 0")    
# a = int(input("Enter number: "))
# try:
#    result = 10/a
# except Exception as err:
#     print(f"sorry there is an error{err} ") 
# else:
#     print(f"The result is {result}")
# finally:
#     print("Execution complete!")           


# age = int(input("Enter age: "))

# if age < 18:
#     raise Exception("You are not eligible")

# print("You can vote")    

age = int(input("Enter age: "))
try:
    if age < 18:
        raise ValueError(" You are not eligible")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"The error is{err}")        

print("You can vote")