class Product:
    def __init__(self, name: str, buy_price: float, sell_price: float, availability: int, total_profit=0):
        self.id = 1
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.availability = availability
        self.total_profit = total_profit


class ShopKeeper:
    def __init__(self, balance: float):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance
