text = input("Enter a string: ")
reverse = text[::-1]

if text == reverse:
    print("The string is palindrome")
else:
    print("The string is not palindrome")