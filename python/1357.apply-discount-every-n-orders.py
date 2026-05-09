from itertools import starmap


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.products = dict(zip(products, prices))
        self.sale = n
        self.current = 0
        self.discount = discount
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current += 1
        discount = self.discount if self.current % self.sale == 0 else 0
        return sum(starmap(lambda x, y: self.products[x] * y, zip(product, amount))) * ((100 - discount) / 100)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)