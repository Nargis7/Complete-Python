colors = ("red", "blue", "green", "red")

print(colors.count("red"))

print(colors.index("blue"))

# colors[0] = "black"  -> value not changed in tuple
print(colors)

# tuple unpacking
a, b, c, d = colors
print(a)
print(b)
print(c)
print(d)