from Couple import *


class Square:
    __c1: Couple
    __c2: Couple
    __c3: Couple
    __c4: Couple
    __number: int
    __round: int

    def __init__(self, num: int, rnd: int, cLst: list[Couple] = None):
        self.__number: int = num
        self.__round: int = rnd
        if cLst is None:
            return
        if not len(cLst) == 4:
            raise ValueError
        self.__c1 = cLst[0]
        self.__c2 = cLst[1]
        self.__c3 = cLst[2]
        self.__c4 = cLst[3]

    def setCouples(self, lst: list[Couple]):
        if self.__c1:
            raise Exception
        if not len(lst) == 4:
            raise ValueError
        self.__c1 = lst[0]
        self.__c2 = lst[1]
        self.__c3 = lst[2]
        self.__c4 = lst[3]

    def __str__(self):
        rtn = ""
        rtn += f"####### SQUARE {self.__number:02} of ROUND {self.__round:02} #######\n"
        rtn += f"{self.__c1}\n"
        rtn += f"{self.__c2}\n"
        rtn += f"{self.__c3}\n"
        rtn += f"{self.__c4}\n"
        rtn += "#####################################\n"
        return rtn

    def save(self):
        self.__c1.save()
        self.__c2.save()
        self.__c3.save()
        self.__c4.save()


if __name__ == "__main__":
    cp1, cp2, cp3, cp4 = TEST_get_test_Couples(4)
    sq = Square(1, 0, [cp1, cp2, cp3, cp4])
    print(sq)
