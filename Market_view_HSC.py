# Programa de analise stock
import function_stock

month_usage = 0

while True:
    selection = input("Would you like to A) analyse a stock, B) see the buy list, c) see the sell list or D) to Exist? ")

    select = selection.capitalize()

    if select == "A":
        function_stock.market_view()
        month_usage += 1
    elif select == "B":
        print("THE BUY LIST")
        buy = function_stock.get_buy_list()
        BB = sorted(buy, key=lambda k: k["Name"])

        for i in BB:
            print(f"{i}")

    elif select == "C":
        print("THE BUY LIST")
        sell = function_stock.get_sell_list()
        SL = sorted(sell, key=lambda k: k["Name"])

        for i in SL:
            print(f"{i}")
    else:
        break
