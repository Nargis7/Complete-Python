a = {1, 2, 3, 4, 5}

b = {4, 5, 6, 7, 8}

# union of sets -> combines all unique elements from both sets
c = a.union(b)
print(c) #{1, 2, 3, 4, 5, 6, 7, 8}
# intersection of sets -> finds common elements between both sets
c = a.intersection(b)
print(c) #{4, 5}
# difference of sets -> finds elements in the first set but not in the second
c = a.difference(b)
print(c) #{1, 2, 3}
# symmetric difference of sets -> finds elements in either set but not in both
c = a.symmetric_difference(b)
print(c) #{1, 2, 3, 6, 7, 8}

# duplicate values in a list
a = [10, 20, 30, 40, 10, 20]
unique_values = set(a)
print(unique_values) #{10, 20, 30, 40}


print(a | b) # union
print(a & b) # intersection
print(a - b) # difference
print(a ^ b) # symmetric difference