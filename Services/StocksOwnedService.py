import datetime
from Models.StocksOwned import StocksOwned
import StockService
from ..DB import DBAutomation as DB

def getStocksOwned(profileID):
    conn = DB.getDBConection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stocksOwned WHERE profileID = ?", (profileID,))
    rows = cursor.fetchall()
    conn.close()
    stocks_owned = [StocksOwned(*row) for row in rows]
    return stocks_owned

def BuySellStocks(stockCipher: str, amountToBuyOrSell: int, profile_id: int, transaction_type: str):
    # Get current datetime
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the stock details
    stock = StockService.getStock(stockCipher)
    if stock:
        # Calculate the total transaction amount
        total_amount = stock.currentPrice * amountToBuyOrSell

        # Get the current stocks owned by the profile
        current_stocks_owned = getStocksOwned(profile_id)
        
        # Check if the profile already owns this stock
        existing_stock = next((x for x in current_stocks_owned if x.stockID == stock.id), None)
        
        if existing_stock:
            # Update existing stocks owned
            if transaction_type.lower() == 'buy':
                # Increment the units owned and calculate new purchase price
                new_units_owned = existing_stock.unitsowned + amountToBuyOrSell
                new_purchase_price = ((existing_stock.purchasePrice * existing_stock.unitsowned) + total_amount) / new_units_owned
                conn = DB.getDBConection()
                cursor = conn.cursor()
                cursor.execute("UPDATE stocksOwned SET unitsowned = ?, purchasePrice = ? WHERE id = ?", (new_units_owned, new_purchase_price, existing_stock.id))
                conn.commit()
                conn.close()
            elif transaction_type.lower() == 'sell':
                if existing_stock.unitsowned >= amountToBuyOrSell:
                    # Calculate profit or loss
                    profit_loss = (amountToBuyOrSell * stock.currentPrice) - (amountToBuyOrSell * existing_stock.purchasePrice)
                    
                    # Update existing stocks owned
                    new_units_owned = existing_stock.unitsowned - amountToBuyOrSell
                    conn = DB.getDBConection()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE stocksOwned SET unitsowned = ?, sellPrice = ?, profitLoss = ?, sellDate = ? WHERE id = ?", (new_units_owned, stock.currentPrice, profit_loss, current_date, existing_stock.id))
                    conn.commit()
                    conn.close()
                else:
                    print("Insufficient units owned for selling")
        else:
            # Insert new row for stocks owned
            if transaction_type.lower() == 'buy':
                purchase_price = stock.currentPrice
            else:
                purchase_price = 0.0  # or any default value for sell transactions
            conn = DB.getDBConection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stocksOwned (name, stockID, profileID, purchaseDate, purchasePrice, unitsowned) VALUES (?, ?, ?, ?, ?, ?)",
                           (stock.name, stock.id, profile_id, current_date, purchase_price, amountToBuyOrSell))
            conn.commit()
            conn.close()
    else:
        print("Stock not found")