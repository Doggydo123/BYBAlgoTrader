from Models.HistoricalData import HistoricalData
from DB import DBAutomation as DB

def getAllHistoricalDataForStock(stockCipher: str):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historicalData WHERE name = ?", (stockCipher,))
    rows = cursor.fetchall()
    conn.close()
    historical_data = [HistoricalData(*row) for row in rows]
    return historical_data

def getPeriodOfHistoricalDataForStock(stockCipher: str, startDate: str, endDate: str):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historicalData WHERE name = ? AND date BETWEEN ? AND ?", (stockCipher, startDate, endDate))
    rows = cursor.fetchall()
    conn.close()
    historical_data = [HistoricalData(*row) for row in rows]
    return historical_data

def insertHistoricalData(data):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO historicalData (name, stockID, date, priceHigh, priceLow, priceAverage, volume, adjustedClose, marketCap)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (data.name, data.stockID, data.date, data.priceHigh, data.priceLow, data.priceAverage, data.volume, data.adjustedClose, data.marketCap))
    conn.commit()
    conn.close()

def insertHistoricalDataList(data_list):
    for data in data_list:
        insertHistoricalData(data)