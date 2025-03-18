import sys

def all_stocks():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    args = sys.argv[1].replace(' ', '').split(',')

    if '' in args:
        return

    for arg in args:
        expression = arg.capitalize()

        if expression in COMPANIES:
            print(expression, 'stock price is', STOCKS[COMPANIES[expression]])
        elif expression.upper() in STOCKS:
            expression = expression.upper()
            for j in COMPANIES:
                if COMPANIES[j] == expression:
                    print(expression, 'is a ticker symbol for', j)
        else:
            print(expression.capitalize(), 'is an unknown company or an unknown ticker symbol')

if __name__ == '__main__':
    all_stocks()