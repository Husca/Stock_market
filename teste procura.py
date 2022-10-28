import json


with open("US-Stock-Symbols.json", "r") as Stock_symbol_file:  # Json file of Stocks to buy
    SS_list = json.load(Stock_symbol_file)

    symbol_ask = input("Enter the stock name: ")

    for i in SS_list:
        if i["Name"] == symbol_ask:
            print(i['Symbol'])










