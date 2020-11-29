my_string = """This is my first line,
this is my second line, and...

...this is my fourth line!"""

m = my_string.split('\n', 2)[0]
n = my_string.split('\n', 2)[1]
p = my_string.split('\n', 2)[2]

print(m)
print(n)
print(p)