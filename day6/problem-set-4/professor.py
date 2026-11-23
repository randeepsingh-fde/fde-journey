import random

while True:
    try:
        level = int(input("Level: "))
        if level == 1 or level == 2 or level == 3:
            break
        else:
            print("Enter a valid level.")
    except:
        pass

if level == 1:
    for i in range(10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        print(x,"+",y,"=")
        answer = int(input("Input the answer: "))
        for j in range(2):
            if answer != (x+y):
                print("EEE")
                answer = input("Input the answer: ")
        print("Correct")

elif level == 2:
    for i in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            print(x,"+",y,"=")
            answer = int(input("Input the answer: "))
            for j in range(2):
                if answer != (x+y):
                    print("EEE")
                    answer = input("Input the answer: ")
            print("Correct")

elif level == 3:
    for i in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            print(x,"+",y,"=")
            answer = int(input("Input the answer: "))
            for j in range(2):
                if answer != (x+y):
                    print("EEE")
                    answer = input("Input the answer: ")
            print("Correct")