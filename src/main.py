"""
Importing Relevant Packages
"""
import pandas as pd
from market_data import MarketDataYFinance

# Configurations of Libraries
pd.set_option('display.max_columns', 500)

def main() -> None:
    """
      Specify Ticker and Start/Stop Dates
    """
    start = '2020/01/01'
    stop = '2022/06/30'

    tsla = MarketDataYFinance("TSLA", start, stop)
    tsla_price = tsla.price_df()
    print(tsla_price)
    return None


if __name__ == '__main__':
    print("Executing Code")
    main()
    print("Finished Executing Code")
