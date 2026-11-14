def main():
    time = input("Enter the time(HH:MM): ")

    decimal_time = convert(time)

    if 7.0 <= decimal_time <= 8.0:
            print("Breakfast Time")
    elif 12.00 <= decimal_time <= 13.00:
            print("Lunch Time")
    elif 18.00 <= decimal_time <= 19.00:
            print("Dinner Time")

def convert(time):
    hours, minutes = time.split(":")

    hours1 = int(hours)
    minutes1 = int(minutes)

    decimal_time = hours1 + (minutes1/60)

    return decimal_time

if __name__ == "__main__":
      main()