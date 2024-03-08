import datetime
import time
from Models.HistoricalData import HistoricalData
from Models.Profile import Profile
from Models.Stock import Stock
from Services.HistoricalDataService import getAllHistoricalDataForStock, getPeriodOfHistoricalDataForStock, insertHistoricalData, insertHistoricalDataList
from Services.ProfileService import insertProfile, getProfileById
from Services.StockService import getStock, getStocks, insertStock, insertStocks
from Services.StocksOwnedService import BuySellStocks, getStocksOwned

def testDBProfileJob():
    print("Test Profile insert")
    time.sleep(5)  # Example: sleep for 5 seconds
    profile = Profile(name="John", lastname="Doe", email="john.doe@example.com", username="johndoe", address="123 Main St", accountCreationDate="2022-01-01", accountType="Standard")
    id = insertProfile(profile)
    print("new profile ID",id)
    profile = getProfileById(id)
    print(profile)


def createProfile():
    # Creating a sample profile
    profile = Profile(
        name="John",
        lastname="Doe",
        email="john.doe@example.com",
        username="johndoe",
        address="123 Main St",
        accountCreationDate=datetime.date.today(),
        accountType="Standard"
    )
    # Insert the profile into the database
    profile_id = insertProfile(profile)
    print("New profile ID:", profile_id)
    
    # Inserting sample stocks
    stock1 = Stock(
        symbol="ABC",
        name="Company ABC",
        description="Tech Company",
        industry="Technology",
        sector="IT",
        marketCap=1000000,
        dividendYield=0.05,
        currentPrice=100.0
    )
    stock2 = Stock(
        symbol="DEF",
        name="Company DEF",
        description="Pharma Company",
        industry="Pharmaceuticals",
        sector="Health Care",
        marketCap=750000,
        dividendYield=0.03,
        currentPrice=75.0
    )
    insertStock(stock1)
    insertStock(stock2)
    
    return profile_id

def testDBStocksOwnedJob():
    print("Creating a profile and inserting stocks...")
    # Create a profile first and insert sample stocks
    profile_id = createProfile()

    # Test getStocksOwned
    print("Testing getStocksOwned:")
    stocks_owned = getStocksOwned(profile_id)
    print("Stocks owned by profile", profile_id, ":")
    for stock in stocks_owned:
        print(stock)
    
    # Test BuySellStocks
    print("\nTesting BuySellStocks:")
    # Assuming a valid stockCipher exists in your system for testing purposes
    stock_cipher = "ABC"
    # Assuming a valid amountToBuyOrSell for testing purposes
    amount_to_buy_or_sell = 10
    # Assuming a valid transaction_type (either 'buy' or 'sell')
    transaction_type = "buy"
    BuySellStocks(stock_cipher, amount_to_buy_or_sell, profile_id, transaction_type)
    print("Transaction complete.")


def testDBHistoricalJob():
    # Test insertHistoricalData
    print("Testing insertHistoricalData:")
    # Create a sample historical data object
    data = HistoricalData(
        name="Company ABC",
        stockID=1,
        date=datetime.date(2023, 1, 1),
        priceHigh=110.0,
        priceLow=90.0,
        priceAverage=100.0,
        volume=10000,
        adjustedClose=100.0,
        marketCap=1000000
    )
    # Insert the sample historical data
    insertHistoricalData(data)
    print("Inserted historical data successfully.")

    # Test insertHistoricalDataList
    print("\nTesting insertHistoricalDataList:")
    # Create a list of sample historical data objects
    data_list = [
        HistoricalData(
            name="Company ABC",
            stockID=1,
            date=datetime.date(2023, 1, 2),
            priceHigh=115.0,
            priceLow=95.0,
            priceAverage=105.0,
            volume=12000,
            adjustedClose=105.0,
            marketCap=1100000
        ),
        HistoricalData(
            name="Company ABC",
            stockID=1,
            date=datetime.date(2023, 1, 3),
            priceHigh=112.0,
            priceLow=92.0,
            priceAverage=102.0,
            volume=10500,
            adjustedClose=102.0,
            marketCap=1050000
        )
    ]
    # Insert the list of sample historical data
    insertHistoricalDataList(data_list)
    print("Inserted list of historical data successfully.")

    # Test getAllHistoricalDataForStock
    print("\nTesting getAllHistoricalDataForStock:")
    stockCipher = "ABC"
    historical_data = getAllHistoricalDataForStock(stockCipher)
    print("Historical data for stock with cipher", stockCipher, ":")
    for data in historical_data:
        print(data)

    # Test getPeriodOfHistoricalDataForStock
    print("\nTesting getPeriodOfHistoricalDataForStock:")
    start_date = "2023-01-01"
    end_date = "2023-01-02"
    historical_data_period = getPeriodOfHistoricalDataForStock(stockCipher, start_date, end_date)
    print("Historical data for stock with cipher", stockCipher, "between", start_date, "and", end_date, ":")
    for data in historical_data_period:
        print(data)