# with open("todo.txt", "w") as file:
#     file.write("Buy Groceries\n")
#     file.write("Learn Python\n")

with open("todo.txt", "r") as file:
    content = file.read()

print(content)