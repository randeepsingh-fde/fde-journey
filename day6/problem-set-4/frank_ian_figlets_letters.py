import pyfiglet

str = input("Enter a String: ")
font = input("Specify the font: ")
f = pyfiglet.figlet_format(str, font)
print(f)