import sys
import requests
     
if len(sys.argv)<2:
        sys.exit("Too few arguments")
elif len(sys.argv)>2:
        sys.exit("Too many arguments")

try:
    amount = float(sys.argv[1])
except ValueError:
       sys.exit("Argument is not a number.")

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=37eccb6e11bfc1f7d5b2421ee96b219861a0bce9b8088284c85bbba17ae752bc"

response = requests.get(url)

data = response.json()

price  = float(data["data"]["priceUsd"])

value = amount*price
print(f"${value:,.4f}")