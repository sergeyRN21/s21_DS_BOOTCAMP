import sys

def get_company_info(ticker: str):
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

    ticker_upper = ticker.upper()
    
    if ticker_upper in STOCKS:
        for company, value in COMPANIES.items():
            if value == ticker_upper:
                company_name = company
                break
        price = STOCKS[ticker_upper]
        print(f"{company_name} {price}")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_company_info(sys.argv[1])