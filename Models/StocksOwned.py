class StocksOwned:
    def __init__(self, name, stockID, profileID, purchaseDate, purchasePrice, sellDate, sellPrice, profitLoss, transactionType, unitsowned):
        self.name = name
        self.stockID = stockID
        self.profileID = profileID
        self.purchaseDate = purchaseDate
        self.purchasePrice = purchasePrice
        self.sellDate = sellDate
        self.sellPrice = sellPrice
        self.profitLoss = profitLoss
        self.transactionType = transactionType
        self.unitsowned = unitsowned