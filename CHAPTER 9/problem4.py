word = "Donkey"

with open("CHAPTER 9/filee.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")

with open("CHAPTER 9/filee.txt", "w") as f:
    f.write(contentNew)