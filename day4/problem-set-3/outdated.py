months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Enter the Date: ")

while True:
    date = input("Enter the Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        else:
            month_name, day, year = date.split()
            month = months.index(month_name.title()) + 1
            day = int(day.rstrip(","))
            year = int(year)

        if month < 1 or month > 12 or day < 1 or day > 31:
            continue

    except ValueError:
        continue

    print(f"{year}-{month:02}-{day:02}")
    break