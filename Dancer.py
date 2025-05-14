from Gender import Gender
from frac import Fraction


class Dancer:
    def __init__(self):
        self._name = ""
        self.__id = ""
        self._gender = ""
        self._present = False
        self._dancedLast = 0
        #TODO: implement num_danced as new fraction class
        self._dancedFactor: Fraction = Fraction(0, 1)

    def set_vals(self, name: str, id: str, gender: str, present: bool, last: int = 0,
                 num: Fraction = Fraction(0, 1)) -> None:
        """
        Sets the values of the dancer.
        """
        self._name = name
        self.__id = id
        self._gender = gender
        self._present = present
        self._dancedLast = last
        self._dancedFactor = num

    def print_full_data(self):
        print(f"Name: {self._name}\nID: {self.__id}\nGender: {self._gender}\nPresent: {self._present}\n"
              f"DancedLast: {self._dancedLast}\nDancedFactor: {self._dancedFactor}")

    def __str__(self):
        return self._name

    def __format__(self, format_spec):

        if not format_spec:
            return str(self)
        rtn = ""
        # when formatted with + one can add additional information to the name of the Dancer
        if format_spec[0] == "+":
            match format_spec[1]:
                case "n":  # the number of danced rounds
                    return str(self) + f"[l:{self._dancedLast}, f:{self._dancedFactor}]"
                case "g":  # the gender
                    return str(self) + f"[g:{self._gender}]"
                case "p":  # presence (True / False)
                    return str(self) + f"[p:{self._present}]"
                case "a":  # all of the above
                    return str(self) + f"[l:{self._dancedLast}, f:{self._dancedFactor}, g:{self._gender:3}, p:{self._present}]"
                case _:  # wrong specifier given, just returning the string
                    return str(self) + f"[unknown spec {format_spec}]"
        try:
            length = int(format_spec[1:])
        except ValueError:
            print("Wrong format spec")
            return "ERROR"
        if len(self._name) >= length:
            return self._name[:length]
        if format_spec[0] == "<":
            for i in range(length - len(self._name)):
                rtn += " "
        rtn += self._name
        if format_spec[0] == ">":
            for i in range(length - len(self._name)):
                rtn += " "
        return rtn

    def danced(self, round: int):
        self._dancedLast = round
        self._dancedFactor = self._dancedFactor.add_split(1, 1)

    def notDanced(self):
        self._dancedFactor = self._dancedFactor.add_split(0, 1)

    def resetNumbers(self):
        self._dancedLast = 0
        self._dancedFactor = Fraction(0, 0)

    def save(self):
        try:
            with open(f"./dnc/{self.__id}.dnc", "w") as f:
                if self._present:
                    prs = "1"
                else:
                    prs = "0"
                f.writelines(
                    [f"{self._name}\n", f"{self.__id}\n", f"{self._gender}\n", f"{prs}\n", f"{self._dancedLast}\n",
                     f"{self._dancedFactor}"])
        except FileNotFoundError:

            print("File not found")

    def is_present(self):
        return self._present

    def switch_presence(self):
        self._present = not self._present

    def getName(self):
        return self._name

    def getLastDanced(self) -> int:
        return self._dancedLast
    
    def getDancedFactor(self) -> Fraction:
        return self._dancedFactor

    def getGender(self) -> str:
        return self._gender

    def getId(self) -> str:
        return self.__id


def loadDancer(id: str) -> Dancer | None:
    """
    Loads a Dancer from dnc directory if the file exists
    :param id: The id used to save the dancer
    :returns: The dancer with entered id or None if {id}.dnc does not exist
    """
    try:
        with open(f"./dnc/{id}.dnc", "r") as f:
            name, id, gender, present_str, last_str, num_str = f.read().split("\n")
            rtn = Dancer()
            present = bool(int(present_str))
            f1_str, f2_str = num_str.split("/")
            rtn.set_vals(name, id, gender, present, int(last_str), Fraction(int(f1_str), int(f2_str)))
            return rtn
    except FileNotFoundError:
        print(f"No Dancer with id [{id}] found")
        return None


def loadDancerFile(file: str) -> Dancer:
    if file.endswith(".dnc"):
        with open(file, "r") as f:
            name, id, gender, present_str, last_str, fact_str = f.read().split("\n")
            rtn = Dancer()
            present = bool(int(present_str))
            f1_str, f2_str = fact_str.split("/")
            rtn.set_vals(name, id, gender, present, int(last_str), Fraction(int(f1_str), int(f2_str)))
            return rtn
        

def existDancer(id: str) -> bool:
    """
    Checks if a dancer with the given id exists in the dnc directory
    :param id: The id used to save the dancer
    :returns: True if the dancer exists, False otherwise
    """
    try:
        with open(f"./dnc/{id}.dnc", "r") as f:
            return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    dancer = Dancer()
    dancer.set_vals("Julian Keune", "370452", "b", True, 5, Fraction(1, 2))
    dancer.save()
    dancer2 = loadDancer("370452")
    d3 = loadDancerFile("./dnc/370452.dnc")
    dancer2.print_full_data()
    print(f"{dancer2:+a}")
    d3.danced(6)
    print(f"{d3:+n}")
