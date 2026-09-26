num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit ** digits
    num = num // 10

if original == sum_digits:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")