import os

from Dancer import *


def IPT_await(specials=None) -> [str, bool]:
    if specials is None:
        specials = []
    while True:
        ipt = input("Awaiting input...")
        if ipt in specials:
            return ipt, True
        if ipt.isnumeric():
            return ipt, False
        else:
            print("Wrong Input!")
            print(f"expected number or {specials}")


def get_full_data():
    dnc = loadDancer(IPT_await()[0])
    dnc.print_full_data()


def load_data_base() -> list[Dancer]:
    rtn = []
    for file in os.listdir("./dnc"):
        if file.endswith(".dnc"):
            rtn.append(loadDancerFile(f"./dnc/{file}"))
    return rtn


def get_present_dancers(lst: list[Dancer]) -> list[Dancer]:
    rtn = []
    for dnc in lst:
        if dnc.is_present():
            rtn.append(dnc)
    return rtn



def sort_list_by_num_danced(lst: list[Dancer]) -> list[Dancer]:
    rtn = []
    while lst:
        minimum = 1000
        for dnc in lst:
            if dnc.getNumDanced() < minimum:
                minimum = dnc.getNumDanced()
        for dnc in lst:
            if dnc.getNumDanced() == minimum:
                rtn.append(dnc)
                lst.remove(dnc)
    return rtn



if __name__ == "__main__":
    for dancer in get_present_dancers(sort_list_by_num_danced(load_data_base())):
        print(dancer)
