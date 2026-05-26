num = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
if(num > num2):
    print("First number is greater than second number")
elif(num2 > num):
    print("Second number is greater than first number")
elif(num == num2):
    print("Both numbers are equal")    
else:
    print("Invalid input!")    
