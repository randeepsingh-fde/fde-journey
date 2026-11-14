x = int(input("Enter the first digit: "))
operation = input("What operation do you want to perform (+,-,*,/): ")
y = int(input("Enter the second digit: "))

if operation == "+":
    print(f"{x+y:.1f}")
elif operation == "-":
    print(f"{x-y:.1f}")
elif operation == "*":
    print(f"{x*y:.1f}")
else:
    print(f"{x/y:.1f}")