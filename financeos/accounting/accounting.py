"""
FinanceOS Accounting Engine
"""


class Accounting:

    def __init__(self):
        self.revenue = 0
        self.expenses = 0


    def add_revenue(self, amount):
        self.revenue += amount


    def add_expense(self, amount):
        self.expenses += amount


    def profit(self):
        return self.revenue - self.expenses



if __name__ == "__main__":

    accounts = Accounting()

    accounts.add_revenue(100000)
    accounts.add_expense(35000)

    print("========== ACCOUNTING REPORT ==========")
    print("Revenue :", accounts.revenue)
    print("Expenses :", accounts.expenses)
    print("Net Profit :", accounts.profit())