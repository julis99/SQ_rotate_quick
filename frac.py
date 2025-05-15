class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator
        if self.numerator == self.denominator:
            if self.numerator == 0:
                self.float = 0
            else:
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

    def realEquals(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def add_split(self, add_to_num: int, add_to_den: int):
        return Fraction(self.numerator + add_to_num, self.denominator + add_to_den)


def FRAC_get_permutation(lst: list[Fraction], val: Fraction, used: list[int]) -> tuple[int, list[int]]:
    for i, frac in enumerate(lst):
        if i in used:
            continue
        if val.realEquals(frac):
            return i, used + [i]
    raise ValueError


def FRAC_sort_list_to_permutation(lst: list[Fraction]) -> list[int]:
    """
    Sorts the given list of Fraction objects to determine a permutation of their indices
    that corresponds to the sorted order of fractions by their float values.

    :param lst: A list containing Fraction objects to sort.
    :type lst: list[Fraction]
    :return: A list of integers representing the permutation of indices that sorts
        the given list based on the float value of its elements.
    :rtype: list[int]
    """
    srt = sorted(lst, key=lambda x: x.float)
    rtn = []
    used = []
    for item in srt:
        idx, used = FRAC_get_permutation(lst, item, used)
        rtn.append(idx)
    return rtn


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    f6 = f1 / f2
    arr = [f1, f2, f3, f4, f5, f6]
    new_idx = FRAC_sort_list_to_permutation(arr)
    for idx in new_idx:
        print(arr[idx])
