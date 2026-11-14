# x = int(input("Enter the value of X: "))

# if x%2 == 0:
#     print("X is Even")
# else:
#     print("X is Odd")

def main():
    x = int(input("Enter the number want to check if its even or odd: "))
    if is_even(x):
        print("X is Even")
    else:
        print("X is Odd")

# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# def is_even(n):
#     return True if n%2==0 else False

def is_even(n):
    return n%2==0

main()