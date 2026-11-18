list = {}
while True:
    try:
        item = input().upper()
        if item in list:
            list[item] = list[item] + 1
        else:
            list[item] = 1
    except EOFError:
        break

for item in sorted(list):
    print(list[item], item)