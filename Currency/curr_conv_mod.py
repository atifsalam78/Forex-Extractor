import pandas as pd
from datetime import datetime
import os

def fetch_currency_data(url):
    """Fetch currency data from the website"""
    try:
        data = pd.read_html(url)
        return data[11]
    except Exception as e:
        print(f"Failed to fetch data from {url}: {e}")
        return None

def process_currency_data(data):
    """Process the currency data"""
    if data is None:
        return None
    
    # Rename columns
    data = data.rename(columns={0: "FROM_CURRENCY", 1: "Buying", 2: "CONVERSION_RATE"})
    
    # Drop unnecessary column
    data = data.drop("Buying", axis=1)
    
    # Add new columns
    current_date = datetime.today().strftime("%d-%b-%Y")
    data = data.assign(
        TO_CURRENCY="PKR",
        CONVERSION_DATE=current_date,
        CONVERSION_TYPE="Corporate",
        STATUS_CODE="C",
        CREATION_DATE=current_date,
        CREATED_BY="1115",
        LAST_UPDATE_DATE=current_date,
        LAST_UPDATED_BY="1115",
        LAST_UPDATE_LOGIN="1115"
    )
    data = data.reindex(columns=["FROM_CURRENCY", "TO_CURRENCY", "CONVERSION_DATE", "CONVERSION_TYPE", "CONVERSION_RATE", "STATUS_CODE", "CREATION_DATE", "CREATED_BY", "LAST_UPDATE_DATE", "LAST_UPDATED_BY", "LAST_UPDATE_LOGIN"])
    
    return data

def save_currency_data(data, filename):
    """Save the currency data to a CSV file"""
    try:
        file_path = f"D:/workspace/images/collected_images/{filename}"
        
        data.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save data to {filename}: {e}")

def main():
    
    url = 'https://www.forex.com.pk/open_market_rates.asp'
    data = fetch_currency_data(url)
    processed_data = process_currency_data(data)
    if processed_data is not None:
        print(processed_data)
        save_currency_data(processed_data, "currency_data.csv")

if __name__ == "__main__":
    main()