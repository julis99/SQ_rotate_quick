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

    def __lt__(self, other):
        return self.float < other.float

    def __gt__(self, other):
        return self.float > other.float

    def __le__(self, other):
        return self.float <= other.float

    def __ge__(self, other):
        return self.float >= other.float

    def add_split(self, add_to_num: int, add_to_den: int):
        return Fraction(self.numerator + add_to_num, self.denominator + add_to_den)


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    print(f1 + f2)

