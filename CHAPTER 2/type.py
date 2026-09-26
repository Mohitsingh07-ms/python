a = 31
t = type(a) # class <int>

print(t)

b = 31.5
t = type(b) # class <float>

print(t)

c = "Harry"
t = type(c) # class <str>
print(t)

a = "31.2"
t = type(a)

print(t)

a = "31.5"
b = float(a) # a but the type should be float
t = type(b)

print(t)