def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,343345,757468,6543,65,765,45,55]

f = list(filter(divisible5, a))
print(f)
