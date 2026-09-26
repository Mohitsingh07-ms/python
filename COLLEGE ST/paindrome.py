num = int(input("Enter a number:"))
original = num
reverse = 0
while num>0:
    digits = num % 10
    num = num // 10
    reverse = reverse % 10 + digits
    if ( original == reverse):
        print("the number is palindrome")
    else:
        ("the number is not palindrome")