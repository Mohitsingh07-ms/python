words = ["Donkey", "bad", "ganda"]

with open("CHAPTER 9/fileee.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("CHAPTER 9/fileee.txt", "w") as f:
    f.write(content)       