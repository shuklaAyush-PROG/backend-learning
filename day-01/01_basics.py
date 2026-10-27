print("Hello, Python!")
print("I am learning backend development.")
print(10 + 20)
#age = input("Enter your age: ")
#print(type(age))
#number = int(input("Enter your number: "))

company = "Reliance Industries is a imp mnc of india"
symbol = "RELIANCE"
print(company[-1])
#num1=int(input("enter num1"))
#num2=int(input("enter num2"))
#print(company[num1:num2])
print(company.split())
symbols = ["TCS", "INFY", "ITC"]
prices = [3200, 1600, 450]
stocks = [
    {"symbol": "TCS", "pe": 24, "price": 3200},
    {"symbol": "INFY", "pe": 28, "price": 1600},
    {"symbol": "ITC", "pe": 20, "price": 450},
    {"symbol": "WIPRO", "pe": 35, "price": 280},
]

for symbol, price in zip(symbols, prices):
    print(symbol, price)
for i in range(len(stocks)):
    print(i, stocks[i]["symbol"])
def add(a, b):
    print(a + b)

x = add(2, 3)