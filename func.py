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



def IPT_getBool(msg: str = "Enter y/n")->bool:
    while True:
        if input(msg) == "y":
            return True
        if input(msg) == "n":
            return False

def create_new_Dancer() -> Dancer:
    print("Creating new Dancer")
    new_id = ""
    while True:
        ipt_str = input("Enter Dancer Id: ")
        if ipt_str.isnumeric():
            new_id = ipt_str
            if os.path.exists(f"./dnc/{new_id}.dnc"):
                print(f"The ID {new_id} already exists!, Try again!")
                continue
            break
        print("Wrong Input (ID Expected)\n")
    new_name = input("Enter Dancer Name: ")
    new_gender = ""
    while True:
        ipt_str = input("Enter Dancer Gender (b, g, b/g): ")
        if ["b", "g", "b/g"].__contains__(ipt_str):
            new_gender = ipt_str
            break
        print("Wrong Input (Gender Expected)\n")
    new_presence = IPT_getBool(f"Is {new_name} present? (y/n)")
    new_dnc = Dancer()
    new_dnc.set_vals(new_name,new_id,new_gender,new_presence)
    print("Create the following Dancer?\n\n")
    new_dnc.print_full_data()
    if IPT_getBool("Confirm Creation (y/n)"):
        new_dnc.save()
        return new_dnc
    else:
        print("Deleting Dancer, starting over")
        return create_new_Dancer()






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
