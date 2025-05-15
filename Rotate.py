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

    def reloadLists(self):
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
        self.evaluate(False)

    def evaluate(self, retLists: bool = False) -> None | list[list[Dancer]]:
        """

        :param retLists:
        :return:
        """
        boys = []
        girls = []
        both = []
        for dancer in self._avaible:
            match dancer.getGender():
                case "b":
                    boys.append(dancer)
                case "g":
                    girls.append(dancer)
                case "b/g":
                    both.append(dancer)
                case _:
                    raise ValueError
        hard_couples = min(len(boys), len(girls))
        missing = max(len(boys), len(girls)) - hard_couples
        soft_couples = 0
        if len(both) == missing:
            soft_couples = missing
        elif len(both) > missing:
            soft_couples = missing + ((len(both) - missing) // 2)
        elif len(both) < missing:
            soft_couples = len(both)
        self.possibleSquares = (hard_couples + soft_couples) // 4
        if retLists:
            return [boys, girls, both]
        return None

    def manipulate(self, round: int) -> None:
        self.rounds = round

    def __str__(self):
        rtn = ""
        self.evaluate(False)
        rtn += f"------------------------------------------------------------\n"
        rtn += f"            Details after Round {self.rounds:02}\n"
        rtn += f"------------------------------------------------------------\n"
        if self._avaible:
            rtn += f"Available Dancers ({len(self._avaible)}):\n"
            for dnc in self._avaible:
                rtn += f"    {dnc:+n}\n"
        else:
            rtn += "    NO Dancers available\n"
        rtn += "------------------------\n"
        if self._pausing:
            rtn += f"Pausing Dancers ({len(self._pausing)}):\n"
            for dnc in self._pausing:
                rtn += f"    {dnc:+a}\n"
        else:
            rtn += "    NO pausing Dancers\n"

        rtn += "------------------------\n"
        if self._away:
            rtn += f"Missing Dancers ({len(self._away)}):\n"
            for dnc in self._away:
                rtn += f"    {dnc.getName()}\n"
        else:
            rtn += "    NO missing Dancers\n"
        rtn += "------------------------\n"
        self.evaluate(retLists=False)
        rtn += f"There are currently at most {self.possibleSquares} squares possible\n"
        if len(self._avaible) == 0:
            rtn += "    8 Dancers needed for the first square\n"
        else:
            rtn += f"    {(8 - len(self._avaible)) % 8} Dancers needed for another square\n"
        return rtn

    def newRound(self) -> list[Square]:
        self._currentSquares = []
        boys, girls, both = self.evaluate(True)
        if self.possibleSquares < 1:
            print(f"No Squares possible\n[boys: {len(boys)}]\n[girls: {len(girls)}]\n[both: {len(both)}]\n")
            return []

        self.rounds += 1
        while both:
            if len(boys) <= len(girls):
                boys.append(both.pop(0))
            else:
                girls.append(both.pop(0))
        boys = shuffle_list(boys)
        girls = shuffle_list(girls)
        boys = sort_list_by_last_danced(boys)
        girls = sort_list_by_last_danced(girls)
        unused = boys[(self.possibleSquares*4):] + girls[(self.possibleSquares*4):]
        boys = boys[:(self.possibleSquares * 4)]
        girls = girls[:(self.possibleSquares * 4)]
        num = 0
        while boys:
            cpLst = []
            for i in range(4):
                dnc1 = boys.pop(0)
                dnc1.danced(self.rounds)
                if len(girls) == 1:
                    dnc2 = girls.pop(0)
                elif len(girls) - 1 != 1:
                    dnc2 = girls.pop(random.randint(1, len(girls) - 1))
                else:
                    dnc2 = girls.pop(1)
                dnc2.danced(self.rounds)
                cpLst.append(Couple(dnc1, dnc2))
            self._currentSquares.append(Square(num=num + 1, rnd=self.rounds, cLst=cpLst))
            num += 1
        for sq in self._currentSquares:
            sq.save()
        for dnc in unused:
            dnc.notDanced()
            dnc.save()
        self._avaible += self._pausing
        self._pausing = []
        return self._currentSquares

    def pauseDancer(self, id: str, sendLog: bool = False) -> None:
        for dnc in self._avaible:
            if dnc.getId() == id:
                self._avaible.remove(dnc)
                self._pausing.append(dnc)
                if sendLog:
                    print(f"{dnc} is pausing the next round")
                return
        for dnc in self._pausing:
            if dnc.getId() == id:
                self._pausing.remove(dnc)
                dnc.switch_presence()
                self._away.append(dnc)
                dnc.save()
                if sendLog:
                    print(f"{dnc} is now away")
                return
        for dnc in self._away:
            if dnc.getId() == id:
                self._away.remove(dnc)
                dnc.switch_presence()
                self._avaible.append(dnc)
                dnc.save()
                if sendLog:
                    print(f"{dnc} is now available")
                return

    def resetDancers(self):
        self._currentSquares = []
        self.rounds = 0
        for dnc in self._avaible + self._pausing + self._away:
            dnc.resetNumbers()
            dnc.save()

    def detailed(self) -> str:
        self.evaluate()
        rtn = ""
        if self._avaible:
            rtn += "Available Dancers:\n"
            for dnc in self._avaible:
                rtn += f"    {dnc:+a}\n"
        else:
            rtn += "    NO Dancers available\n"
        rtn += "------------------------\n"
        if self._pausing:
            rtn += "Pausing Dancers:\n"
            for dnc in self._pausing:
                rtn += f"    {dnc:+a}\n"
        else:
            rtn += "    NO pausing Dancers\n"

        rtn += "------------------------\n"
        if self._away:
            rtn += "Missing Dancers:\n"
            for dnc in self._away:
                rtn += f"    {dnc:+a}\n"
        else:
            rtn += "    NO missing Dancers\n"
        rtn += "------------------------\n"
        rtn += f"There are currently at most {self.possibleSquares} squares possible\n"
        if len(self._avaible) == 0:
            rtn += "    8 Dancers needed for the first square\n"
        else:
            rtn += f"    {(8 - len(self._avaible)) % 8} Dancers needed for another square\n"
        return rtn

    def clearAvailable(self):
        for dnc in self._avaible + self._pausing:
            dnc.switch_presence()
            dnc.save()
        self.reloadLists()
        return

    def deleteDancer(self, id: str) -> None:
        for dnc in self._avaible + self._pausing + self._away:
            if dnc.getId() == id:
                if dnc in self._avaible:
                    self._avaible.remove(dnc)
                elif dnc in self._pausing:
                    self._pausing.remove(dnc)
                elif dnc in self._away:
                    self._away.remove(dnc)
                else:
                    raise ValueError("Dancer not found")
                os.remove(f"./dnc/{dnc.getId()}.dnc")
                return
        print("Dancer not found")

    def print_ids(self) -> None:
        print("Registered Dancers:")
        dncs = self._avaible + self._pausing + self._away
        for dnc in sort_list_by_name(dncs):
            print(f"{dnc:>15} : [{dnc.getId()}]")
        print("====================================================================\n")


if __name__ == "__main__":
    rt = Rotate()
    rt.reloadLists()
    lst = rt.newRound()
    for sq in lst:
        print(sq)
    print("====================================================================\n")
    print(rt)
