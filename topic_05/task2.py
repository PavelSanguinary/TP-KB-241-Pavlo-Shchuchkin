import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
data = requests.get(url).json()

rates = {}  
for item in data:
    if item["cc"] == "USD" or item["cc"] == "EUR" or item["cc"] == "PLN":
        rates[item["cc"]] = item["rate"]

amount = float(input("Введіть суму: ").replace(",", "."))
cur = input("Введіть валюту (USD, EUR, PLN): ").strip().upper()
if cur not in rates:
    print("Підтримуються тільки USD, EUR, PLN.")
else:
    result = amount * rates[cur]  
    print(amount, cur, "=", round(result, 2), "UAH")
