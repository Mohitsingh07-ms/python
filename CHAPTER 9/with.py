f = open("CHAPTER 9/file.txt")

data = f.read()

print(data)

f.close()

# the same can be written using with statement like this:
with open("CHAPTER 9/file.txt") as f:
    print(f.read())