#loops
# There are two types of for loop in python
# for loop
# while loop

#for i in range(5):
    #print(i)

#
    #print(i)    


#name = "Nargis Perween"

#for i in range(10):
   # print(name[i])

name1 = "Nature" 
#for i in range(len(name1)):
    #print(name1[i])   

#i = 1
#while (i <= 7):
   # print(i)
    #i +=1    

name = "Nargis Perween"
#print(len(name))   
#for char in name:
    #print(char) 

#Break -> stops the loop and continue -> skips the current iteration and moves to the next one

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)   

# print('\n')

# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#          print(i)  

# separate each digit of a number

# a = 256
# num = int(input("Enter Your Number: "))

# while a > 0:
#     print(a % 10)
#     a = a // 10

# accept a number and print its reverse
# num = int(input("Enter Your Number: "))
# original = num
# reverse = 0 
# while num !=0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# if original == reverse:
#     print("The number is Palindromic Number") 
# else:
#     print("The number is not plaindromic Number")       


# create a random number guessing game
import random

num = random.randint(1,11)

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")