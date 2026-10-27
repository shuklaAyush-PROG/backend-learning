with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python for backend development.\n")
    file.write("Today I am learning file handling.")
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)    