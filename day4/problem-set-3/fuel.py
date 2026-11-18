while True:
    try:
        fuel = input("Enter the fuel in fraction (X/Y): ")
        top, bottom = fuel.split("/");
        top_int = int(top)
        bottom_int = int(bottom)
        if top_int > bottom_int or top_int < 0 or bottom_int < 0:
            raise ValueError
        percentage = (top_int/bottom_int)*100
    except ValueError:
        pass
    except ZeroDivisionError:
        print("Denominator can not be 0")
    else:
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            percentage = round(percentage)
            print(percentage,"%")
        break