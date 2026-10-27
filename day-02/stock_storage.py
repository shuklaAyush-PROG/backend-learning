import json
stocks = [
    {"symbol": "TCS", "price": 3200},
    {"symbol": "INFY", "price": 1600},
    {"symbol": "ITC", "price": 450}
]
with open("stocks.json","w") as file:
    json.dump(stocks,file,indent=4)
with open("stocks.json","r") as file:
    stocks=json.load(file)
print(stocks)    