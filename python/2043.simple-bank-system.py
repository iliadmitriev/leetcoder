class Bank:
    def __init__(self, balance: list[int]):
        self.accounts = [0] * (len(balance) + 1)

        for i in range(len(balance)):
            self.accounts[i + 1] = balance[i]

    def _valid(self, account: int) -> bool:
        return 1 <= account < len(self.accounts)

    def _enough(self, account: int, money: int) -> bool:
        return self.accounts[account] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self._valid(account1)
            or not self._valid(account2)
            or not self._enough(account1, money)
        ):
            return False

        self.accounts[account1] -= money
        self.accounts[account2] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False

        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account) or not self._enough(account, money):
            return False

        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)