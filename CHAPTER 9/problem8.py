with open("CHAPTER 9/this.txt") as f:
    content = f.read()

with open("CHAPTER 9/this_copy.txt", "w") as f:
    f.write(content)    