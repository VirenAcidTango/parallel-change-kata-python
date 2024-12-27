class ShoppingCart:
    prices: list[float]

    def __init__(self):
        self.prices = []

    def add(self, price) -> None:
        self.prices.append(price)

    def calculate_total_price(self) -> float:
        return sum(self.prices)


    def has_discount(self) -> bool:
        return any(price >= 100 for price in self.prices)

    def number_of_products(self) -> int:
        return len(self.prices)
