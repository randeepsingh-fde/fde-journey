# ends the code immediately

# try:
#     x = int(input("enter x: "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print("x is",x)

# Using a loop, it keeps asking untill the right input is recieved

while True:
    try:
        x = int(input("enter x: "))
        break
    except ValueError:
        print("x is not an integer")

print("x is",x)    