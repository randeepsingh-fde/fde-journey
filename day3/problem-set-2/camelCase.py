string = input("Enter a String in camelCase: ")
new_string = ""

for i in string:
    if i.isupper():
        new_string = new_string + "_"
    new_string = new_string + i


lowercase_string = new_string.lower()

print(lowercase_string)