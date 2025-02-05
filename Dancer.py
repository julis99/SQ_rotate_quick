class Dancer:
    def __init__(self):
        self._name = ""
        self.__id = ""
        self._gender = ""
        self._present = False
        self._numDanced = 0

    def set_vals(self, name: str, id: str, gender: str, present: bool, num: int):
        self._name = name
        self.__id = id
        self._gender = gender
        self._present = present
        self._numDanced = num

    def print_full_data(self):
        print(f"Name: {self._name}\nID: {self.__id}\nGender: {self._gender}\nPresent: {self._present}\n"
              f"NumDanced: {self._numDanced}")

    def __str__(self):
        return self._name

    def __format__(self, format_spec):
        rtn = ""
        try:
            length = int(format_spec[1:])
        except ValueError:
            print("Wrong format spec")
            return "ERROR"
        if len(self._name) >= length:
            return self._name[:length]
        if format_spec[0] == "<":
            for i in range(length-len(self._name)):
                rtn += " "
        rtn += self._name
        if format_spec[0] == ">":
            for i in range(length-len(self._name)):
                rtn += " "
        return rtn

    def danced(self):
        self._numDanced += 1

    def resetNumDanced(self):
        self._numDanced = 0

    def save(self):
        try:
            with open(f"./dnc/{self.__id}.dnc", "w") as f:
                if self._present:
                    prs = "1"
                else:
                    prs = "0"
                f.writelines(
                    [f"{self._name}\n", f"{self.__id}\n", f"{self._gender}\n", f"{prs}\n", f"{self._numDanced}"])
        except FileNotFoundError:
            print("File not found")

    def is_present(self):
        return self._present

    def switch_presence(self):
        self._present = not self._present

    def getName(self):
        return self._name

    def getNumDanced(self)->int:
        return self._numDanced


def loadDancer(id: str) -> Dancer:
    with open(f"./dnc/{id}.dnc", "r") as f:
        name, id, gender, present_str, num_str = f.read().split("\n")
        rtn = Dancer()
        present = bool(int(present_str))
        rtn.set_vals(name, id, gender, present, int(num_str))
        return rtn


def loadDancerFile(file: str) -> Dancer:
    if file.endswith(".dnc"):
        with open(file, "r") as f:
            name, id, gender, present_str, num_str = f.read().split("\n")
            rtn = Dancer()
            present = bool(int(present_str))
            rtn.set_vals(name, id, gender, present, int(num_str))
            return rtn


if __name__ == "__main__":
    dancer = Dancer()
    dancer.set_vals("Julian Keune", "370452", "b/g", True, 5)
    dancer.save()
    dancer2 = loadDancer("370452")
    dancer2.print_full_data()
