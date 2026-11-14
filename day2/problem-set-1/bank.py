greeting = input()

first_letter = greeting[0]
first_five = greeting[:5]

if first_five == "hello":
    print("$0")
elif first_letter == "h" and first_five != "hello":
    print("$20")
else:
    print("$100")