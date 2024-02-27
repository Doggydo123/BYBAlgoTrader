class HistoricalData:
    def __init__(self, name, stockID, date, priceHigh, priceLow, priceAverage, volume, adjustedClose, marketCap):
        self.name = name
        self.stockID = stockID
        self.date = date
        self.priceHigh = priceHigh
        self.priceLow = priceLow
        self.priceAverage = priceAverage
        self.volume = volume
        self.adjustedClose = adjustedClose
        self.marketCap = marketCap