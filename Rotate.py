import os

from Dancer import *


class Rotate:
    def __init__(self):
        self._avaible: list[Dancer]
        self._pausing: list[Dancer]
        self._away: list[Dancer]
        self.possibleSquares = 0

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


if __name__ == "__main__":
    rt = Rotate()
    rt.reloadlists()
    print(rt)
