import yfinance as yf


class FinancialStatements:

    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.stock = yf.Ticker(self.symbol)

    def show_income_statement(self):

        print("\n========== INCOME STATEMENT ==========")

        income = self.stock.financials

        if income.empty:
            print("Income statement not available.")
            return

        print(income)

    def show_balance_sheet(self):

        print("\n========== BALANCE SHEET ==========")

        balance = self.stock.balance_sheet

        if balance.empty:
            print("Balance sheet not available.")
            return

        print(balance)

    def show_cash_flow(self):

        print("\n========== CASH FLOW ==========")

        cashflow = self.stock.cashflow

        if cashflow.empty:
            print("Cash flow statement not available.")
            return

        print(cashflow)

    def show_all(self):

        self.show_income_statement()
        self.show_balance_sheet()
        self.show_cash_flow()


if __name__ == "__main__":

    fs = FinancialStatements("AAPL")
    fs.show_all()