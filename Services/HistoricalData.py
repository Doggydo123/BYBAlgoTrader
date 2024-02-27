from Models.HistoricalData import HistoricalData
from ..DB import DBAutomation as DB

def getAllHistoricalDataForStock(stockCipher: str):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historicalData WHERE stockCipher = ?", (stockCipher,))
    rows = cursor.fetchall()
    conn.close()
    historical_data = [HistoricalData(*row) for row in rows]
    return historical_data

def getPeriodOfHistoricalDataForStock(stockCipher: str, startDate: str, endDate: str):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historicalData WHERE stockCipher = ? AND date BETWEEN ? AND ?", (stockCipher, startDate, endDate))
    rows = cursor.fetchall()
    conn.close()
    historical_data = [HistoricalData(*row) for row in rows]
    return historical_data
