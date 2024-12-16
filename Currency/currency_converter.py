import pandas as pd
from datetime import datetime
# import time
# import json

try:
        
    # Fetch data from web and convert it into pandas data frame
    url = 'https://www.forex.com.pk/open_market_rates.asp'
    data = pd.read_html(url)
    currency_data = data[11]
    
    currency_data = currency_data.rename(columns={0: "FROM_CURRENCY", 1: "Buying", 2: "CONVERSION_RATE"})
    currency_data = currency_data.drop("Buying", axis=1)
    currency_data["TO_CURRENCY"] = "PKR"
    currency_data["CONVERSION_DATE"] = datetime.today().strftime("%d-%m-%Y")
    currency_data["CONVERSION_DATE"] = pd.to_datetime(currency_data.CONVERSION_DATE)
    currency_data["CONVERSION_TYPE"] = "Corporate"
    currency_data["STATUS_CODE"] = "C"
    currency_data["CREATION_DATE"] = datetime.today().strftime("%d-%m-%Y")
    currency_data["CREATION_DATE"] = pd.to_datetime(currency_data.CREATION_DATE)
    currency_data["CREATED_BY"] = "1115"
    currency_data["LAST_UPDATE_DATE"] = datetime.today().strftime("%d-%m-%Y")
    currency_data["LAST_UPDATE_DATE"] = pd.to_datetime(currency_data.LAST_UPDATE_DATE)
    currency_data["LAST_UPDATED_BY"] = "1115"
    currency_data["LAST_UPDATE_LOGIN"] = "1115"
            

    # currency_usd = currency_data.loc[currency_data["Currency"] == "US Dollar"]
    print("\n", currency_data)
    currency_data.to_csv("currency_data.csv", index=False)
            
except Exception as e:
        print("\nUnable to fetch data from website Or server down --", e)


