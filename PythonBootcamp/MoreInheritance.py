# Parent or Super Class
class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __str__(self):
        return f"{self.number:.{self.places}f}"


# Child Class
class Currency(Decimal):
    def __init__(self, number, places, symbol):
        super().__init__(number, places)
        self.symbol = symbol

    def __str__(self):
        return f"{self.symbol}{super().__str__()}"


print(Decimal(15.6789, 3))
print(Currency(15.6789, 2, '$'))
