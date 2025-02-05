import os
import random

from Dancer import *
from Couple import *
from Square import *
from func import *


class Rotate:
    def __init__(self):
        self._avaible: list[Dancer] = []
        self._pausing: list[Dancer] = []
        self._away: list[Dancer] = []
        self._currentSquares: list[Square] = []
        self.possibleSquares: int = 0
        self.rounds: int = 0

    def reloadlists(self):
        self._avaible = []
        self._pausing = []
        self._away = []
        for file in os.listdir("./dnc"):
            if file.endswith(".dnc"):
                dnc = loadDancerFile(os.path.join("./dnc", file))
                if not dnc.is_present():
                    self._away.append(dnc)
                else:
                    self._avaible.append(dnc)
        self.possibleSquares = len(self._avaible) // 8

    def __str__(self):
        rtn = ""
        if self._avaible:
            rtn += "Available Dancers:\n"
            for dnc in self._avaible:
                rtn += f"    {dnc.getName()}\n"
        else:
            rtn += "    NO Dancers available\n"
        rtn += "------------------------\n"
        if self._pausing:
            rtn += "Pausing Dancers:\n"
            for dnc in self._pausing:
                rtn += f"    {dnc.getName()}\n"
        else:
            rtn += "    NO pausing Dancers\n"

        rtn += "------------------------\n"
        if self._away:
            rtn += "Missing Dancers:\n"
            for dnc in self._away:
                rtn += f"    {dnc.getName()}\n"
        else:
            rtn += "    NO missing Dancers\n"
        rtn += "------------------------\n"
        rtn += f"There are {self.possibleSquares} squares possible\n"
        if len(self._avaible) == 0:
            rtn += "    8 Dancers needed for the first square\n"
        else:
            rtn += f"    {(8 - len(self._avaible)) % 8} Dancers needed for another square\n"
        return rtn

    def newRound(self) -> list[Square]:
        self.rounds += 1
        self._currentSquares = []
        self._avaible = sort_list_by_num_danced(self._avaible)
        self.possibleSquares = len(self._avaible) // 8
        dancing = self._avaible[:(self.possibleSquares*8)]
        num = 1
        while dancing:
            cpLst = []
            for i in range(4):
                dnc1 = dancing.pop(0)
                dnc1.danced()
                if len(dancing) == 1:
                    dnc2 = dancing.pop(0)
                elif len(dancing)-1 != 1:
                    dnc2 = dancing.pop(random.randint(1, len(dancing) - 1))
                else:
                    dnc2 = dancing.pop(1)
                dnc2.danced()
                cpLst.append(Couple(dnc1, dnc2))
            self._currentSquares.append(Square(num=num, rnd=self.rounds, cLst=cpLst))
            num += 1
        for sq in self._currentSquares:
            sq.save()
        return self._currentSquares

    def resetDancers(self):
        self._currentSquares = []
        for dnc in self._avaible + self._pausing + self._away:
            dnc.resetNumDanced()
            dnc.save()







if __name__ == "__main__":
    rt = Rotate()
    rt.reloadlists()
    lst = rt.newRound()
    for sq in lst:
        print(sq)
    print("====================================================================\n")
    print(rt)
