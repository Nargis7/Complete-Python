print("Hello , we are learning python!")

# comment
""" multiple line comment """ 

# variables
name = "Nargis"
age = 21
#print(name)
#print(age)

# naming convention
NargisPerween = "student" # pascal case
nargisPerween = "nargis"  # camel case
nargis_perween = "nargis" # snake case

a = 12
b = 12.34
d = 34j
c = True
#print(type(a)) # int
#print(type(b)) # float
#print(type(d)) #complex
#print(type(name)) # string
#print(type(c)) # boolean

d = "A"
#print(ord(d)) # unique code 65

#convert unique code into number
e = 65
#print(chr(e)) # A

#print(name[0])
#print(name[1])
#print(name[2])
#print(name[3])

# slicing
#print(name[0:4:1])

# type conversion

f = 12
f = str(f)

#print(f)
#print(type(f))

#print(f"my name is {name} and my age is {age}")

#age = int(input("Enter you age: "))
#print(f"you are {age} years old! ")

# arithmetic operators
a = 10
b = 3
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # floor division
print(a % b) # modulus
print(a ** b) # exponentiation

# assignment operators
a = 10
a += 5 # a = a + 5
print(a) # 15
a -= 3 # a = a - 3
print(a) # 12
a *= 2 # a = a * 2
print(a) # 24
a /= 4 # a = a / 4
print(a) # 6.0
a %= 5 # a = a % 5
print(a) # 1.0

# comparison operators
a = 10
b = 20
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

#logical operators
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False
