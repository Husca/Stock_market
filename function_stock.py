import json
from urllib.request import urlopen
import requests


def get_buy_list():
    with open("buy.json", "r") as buy_file:  # Json file of Stocks to buy
        buy_list = json.load(buy_file)
        return buy_list


def get_sell_list():
    with open("sell.json", "r") as sell_file:  # Json file of Stocks to sell
        sell_list = json.load(sell_file)
        return sell_list


def market_view():
    symbol = input("Please enter the stock price: ")

    # To see the overview of the stock
    Api_key = 'NKBDH0ZH8SMTYG2P'

    overview = urlopen(
        'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + symbol + '&apikey=' + Api_key).read()

    data = json.loads(overview)

    # To collect the close price of stock

    params = {'access_key': "1ff86d56c27ffe8c58e5658b858782c9"}

    api_result = requests.get('http://api.marketstack.com/v1/tickers/' + symbol + '/eod/latest', params)

    api_response = api_result.json()

    # Stochastic RSI

    SORHI = urlopen(
        'https://www.alphavantage.co/query?function=STOCHRSI&symbol=' + symbol + '&interval=daily&time_period=10&series_type=close&fastkperiod=6&fastdmatype=1&apikey=' + Api_key).read()
    dat_sorhi = json.loads(SORHI)

    sorsi_date = '2022-10-27'

    res_sorsi = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]

    # Overview of the stock
    print(f"Stock Name: {data['Name']}")
    print(f"Stock sector: {data['Sector']}")

    # Stochastic RSI results
    print(f"The Stochastic RSI result : {res_sorsi}")

    d = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]["FastD"]

    k = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]["FastK"]

    if k == 80 and k >= d:
        print("It's a moment of a price correction because there is a lot of sellers")
    elif k == 30 and k <= d:
        print("It's a moment to buy!")

        # Stock price analysis
    try:
        close = float(api_response['close'])

        print(f"The close price of {data['Name']} - {close} {data['Currency']}")
        print(f"The analyst target price is {data['AnalystTargetPrice']} {data['Currency']}")
        print(
            f"Last 52 week the high level was {data['52WeekHigh']} {data['Currency']} and the low level was {data['52WeekLow']} {data['Currency']}.")
    except:
        print(api_response)

    target = float(data['AnalystTargetPrice'])

    if target > close:
        print("We are ok. The close price is bellow expected price")

        res = target - close

        R = round(res, 2)

        print(f"{api_response['close']} {data['Currency']} is {R} bellow.")

    elif target < close:
        print("We are NOT ok. The close price is above expected price")
        print("It's better to close your positions")

        res = close - target

        R = round(res, 2)

        print(f"{api_response['close']} {data['Currency']} is {R} above.")

        # Moving Average Median

    if data["50DayMovingAverage"] >= data['200DayMovingAverage']:
        print("It's time to buy!")
        print(f"MA50 - {data['50DayMovingAverage']}")
        print(f"MA200 - {data['200DayMovingAverage']}")

    elif data["50DayMovingAverage"] <= data['200DayMovingAverage']:
        print("It's time to wait!")
        print(f"MA50 - {data['50DayMovingAverage']}")
        print(f"MA200 - {data['200DayMovingAverage']}")

    # Ação de comprar ou venda
    buy = get_buy_list()
    sell = get_sell_list()

    name = data["Name"]
    currency = data['Currency']

    if data["50DayMovingAverage"] >= data['200DayMovingAverage'] and target > close:
        buy.append({"Name": name, "Target Price": target, "Currency": currency})
        with open("buy.json", "w") as buy_file:
            buy_file.write(json.dumps(buy))

    elif target < close:
        sell.append({"Name": name, "Price": close, "Target Price": target, "Currency": currency})
        with open("sell.json", "w") as sell_file:
            sell_file.write(json.dumps(sell))


def market_view_list():
    stock_list = []

    while True:
        op = input("Do you wish add a stock to the list Y) or N): ")
        if op.capitalize() == "Y":
            sb = input("Please enter the stock price: ")
            stock_list.append(sb)

        if op.capitalize() == "N":
            for value in stock_list:

                symbol = value

                # To see the overview of the stock
                Api_key = 'NKBDH0ZH8SMTYG2P'

                overview = urlopen(
                    'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + symbol + '&apikey=' + Api_key).read()

                data = json.loads(overview)

                # To collect the close price of stock

                params = {'access_key': "1ff86d56c27ffe8c58e5658b858782c9"}

                api_result = requests.get('http://api.marketstack.com/v1/tickers/' + symbol + '/eod/latest', params)

                api_response = api_result.json()

                # Stochastic RSI

                SORHI = urlopen(
                    'https://www.alphavantage.co/query?function=STOCHRSI&symbol=' + symbol + '&interval=daily&time_period=10&series_type=close&fastkperiod=6&fastdmatype=1&apikey=' + Api_key).read()
                dat_sorhi = json.loads(SORHI)

                sorsi_date = '2022-10-26'

                res_sorsi = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]

                # Overview of the stock
                print(f"Stock Name: {data['Name']}")
                print(f"Stock sector: {data['Sector']}")

                # Stochastic RSI results
                print(f"The Stochastic RSI result : {res_sorsi}")

                d = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]["FastD"]

                k = dat_sorhi['Technical Analysis: STOCHRSI'][sorsi_date]["FastK"]

                if k == 80 and k >= d:
                    print("It's a moment of a price correction because there is a lot of sellers")
                elif k == 30 and k <= d:
                    print("It's a moment to buy!")

                # Stock price analysis

                # print(f"The close price of {data['Name']} - {api_response['close']} {data['Currency']}")
                # print(f"The analyst target price is {data['AnalystTargetPrice']} {data['Currency']}")
                # print(f"Last 52 week the high level was {data['52WeekHigh']} {data['Currency']} and the low level was {data['52WeekLow']} {data['Currency']}.")

                close = float(api_response['close'])
                target = float(data['AnalystTargetPrice'])

                if target > close:
                    print("We are ok. The close price is bellow expected price")

                    res = target - close

                    R = round(res, 2)

                    print(f"{api_response['close']} {data['Currency']} is {R} bellow.")

                elif target < close:
                    print("We are NOT ok. The close price is above expected price")
                    print("It's better to close your positions")

                    res = close - target

                    R = round(res, 2)

                    print(f"{api_response['close']} {data['Currency']} is {R} above.")

                    # Moving Average Median

                    if data["50DayMovingAverage"] >= data['200DayMovingAverage']:
                        print("It's time to buy!")
                        print(f"MA50 - {data['50DayMovingAverage']}")
                        print(f"MA200 - {data['200DayMovingAverage']}")

                    elif data["50DayMovingAverage"] <= data['200DayMovingAverage']:
                        print("It's time to wait!")
                        print(f"MA50 - {data['50DayMovingAverage']}")
                        print(f"MA200 - {data['200DayMovingAverage']}")

                    # Ação de comprar ou venda
                    buy = get_buy_list()
                    sell = get_sell_list()

                    name = data["Name"]
                    currency = data['Currency']

                    if data["50DayMovingAverage"] >= data['200DayMovingAverage'] and target > close:
                        buy.append({"Name": name, "Target Price": target, "Currency": currency})
                        with open("buy.json", "w") as buy_file:
                            buy_file.write(json.dumps(buy))

                    elif target < close:
                        sell.append({"Name": name, "Price": close, "Target Price": target, "Currency": currency})
                        with open("sell.json", "w") as sell_file:
                            sell_file.write(json.dumps(sell))  # In constrution
