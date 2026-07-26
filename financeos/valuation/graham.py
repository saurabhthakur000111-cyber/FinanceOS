import math


class GrahamValuation:

    def __init__(self, eps, book_value):

        self.eps = eps
        self.book = book_value

    def calculate(self):

        return math.sqrt(22.5 * self.eps * self.book)


if __name__ == "__main__":

    graham = GrahamValuation(
        eps=12,
        book_value=45
    )

    print("Graham Value =", round(graham.calculate(), 2))