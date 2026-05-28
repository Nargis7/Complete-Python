a = [10,40,70,30]

# a.append(70)
# a.insert(3,77)
# a.remove(30)
# num = a.index(20)
# print(num)

# a.sort()
# print(a)

# a[0] = 99
# print(a)

# print(a[2])
# print(len(a))
# # for num in a:
# #     print(num)

# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#     print(fruit)

# Print positive and negative numbers

# num = [-45,-56,67,89,-90,45]

# print("Numbers are positive:")
# for i in num:
#     if i >= 0:
#         print(i)

# print("Numbers are negative:")
# for i in num:
#     if i <=0:
#         print(i)
# mean of list elements
num = [10,20,30,40,50]
# total = 0
# for i in num:
#     total += i
# mean = total / len(num)
# print(mean)
# find the largest number in a list
# largest = num[0]
# for i in num:
#     if i >= largest:
#         largest = i
# print(largest)

# second largest number of index in a list
# second_largest = num[0]
# index = 0
# for i in num:
#     if i > second_largest and i != max(num):
#         second_largest = i
#         index = num.index(i)
# print(second_largest)
# print(index)


a = [234,78,89,900,679,78]

largest = a[0]
index = 0
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i
print(f"The largest number is{largest} at index is {index}")        
