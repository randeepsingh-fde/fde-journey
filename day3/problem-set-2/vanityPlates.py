
def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Condition 1: Length must be between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Condition 2: First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Condition 3: Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Conditions 4 and 5: Numbers must be at the end,
    # and the first number cannot be zero
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False

    return True


if __name__ == "__main__":
    main()
