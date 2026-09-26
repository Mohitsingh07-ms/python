num = int(input("Enter a number:"))
a = 0
b = 1
print("Fibonaaci series")
for i in range(num):
    print(a, end=" ")
    c = a + b
    a = b
    b = c