from typing import List
from Models.Stock import Stock
from DB import DBAutomation as DB

def getStock(cipher: str):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock WHERE id = ?", (cipher,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Stock(*row)
    else:
        return None

def getStocks(ciphers: List[str]):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    query = "SELECT * FROM stock WHERE id IN ({})".format(','.join('?' * len(ciphers)))
    cursor.execute(query, ciphers)
    rows = cursor.fetchall()
    conn.close()
    stocks = [Stock(*row) for row in rows]
    return stocks

def insertStock(stock: Stock):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stock (name, description, currentPrice) VALUES (?, ?, ?)",
                   (stock.name, stock.description, stock.currentPrice))
    stock_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return stock_id

def insertStocks(stocks: List[Stock]):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    for stock in stocks:
        cursor.execute("INSERT INTO stock (name, description, currentPrice) VALUES (?, ?, ?)",
                       (stock.name, stock.description, stock.currentPrice))
    conn.commit()
    conn.close()
