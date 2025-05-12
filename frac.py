class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator
        if self.numerator == self.denominator:
            self.float = 1
            return
        if self.denominator == 0:
            raise ZeroDivisionError
        self.float = numerator / denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.float

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __sub__(self, other):
        return self + Fraction(-other.numerator, other.denominator)

    def __truediv__(self, other):
        return self * Fraction(other.denominator, other.numerator)

    def __eq__(self, other):
        return self.float == other.float