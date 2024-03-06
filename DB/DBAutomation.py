import sqlite3


def getDBConection():
    # Establish a connection to the database
    conn = sqlite3.connect('AlgoTrading.db')
    return conn


def setupTables(conn):
    # Create cursor
    cursor = conn.cursor()
    # Create tables
    profileTable(cursor)
    stockTable(cursor)
    stocksOwnedTable(cursor)
    historicalDataTable(cursor)
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def profileTable(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT,
        lastname TEXT,
        email TEXT,
        username TEXT,
        address TEXT,
        accountCreationDate TEXT,
        accountType TEXT,
        stocksOwnedId INTEGER)
        """
    # Execute SQL
    cursor.execute(sql)


def stockTable(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        symbol TEXT,
        name TEXT,
        description TEXT,
        industry TEXT,
        sector TEXT,
        marketCap REAL,
        dividendYield REAL,
        currentPrice REAL)
        """
    # Execute SQL
    cursor.execute(sql)


def stocksOwnedTable(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS stocksOwned (
        FOREIGN KEY(profileID) REFERENCES profile(id),
        name TEXT,
        stockID INTEGER,
        purchaseDate TEXT,
        purchasePrice REAL,
        sellDate TEXT,
        sellPrice REAL,
        profitLoss REAL,
        transactionType TEXT,
        unitsowned INTEGER)
        """
    # Execute SQL
    cursor.execute(sql)


def historicalDataTable(cursor):
    sql = """
        CREATE TABLE IF NOT EXISTS historicalData (
        id INTEGER PRIMARY KEY,
        name TEXT,
        stockID INTEGER,
        date TEXT,
        priceHigh REAL,
        priceLow REAL,
        priceAverage REAL,
        volume INTEGER,
        adjustedClose REAL,
        marketCap REAL)
        """
    # Execute SQL
    cursor.execute(sql)


def setup():
    conn = getDBConection()
    setupTables(conn)
