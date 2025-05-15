import os

from Dancer import *
from frac import FRAC_sort_list_to_permutation


def IPT_await(specials=None, msg="Awaiting input...: ") -> [str, bool]:
    if specials is None:
        specials = []
    while True:
        ipt = input(msg)
        if ipt in specials:
            return ipt, True
        if ipt.isnumeric():
            return ipt, False
        else:
            print("Wrong Input!")
            print(f"expected number or {specials}")


def IPT_command(allowed: list[str], msg: str = "Enter command:") -> str:
    while True:
        ipt_str = input(msg)
        if allowed.__contains__(ipt_str):
            return ipt_str
        print(f"Wrong Input (Expected one of {allowed})\n")


def IPT_getBool(msg: str = "Enter y/n") -> bool:
    while True:
        ipt = input(msg)
        if ipt == "y":
            return True
        if ipt == "n":
            return False


def create_new_Dancer(new_id: str = None) -> Dancer:
    print("Creating new Dancer")
    if new_id:
        if os.path.exists(f"./dnc/{new_id}.dnc"):
            print(f"The ID {new_id} already exists!, Try another one!")
            new_id = None
    if not new_id:
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
    new_dnc.set_vals(new_name, new_id, new_gender, new_presence)
    print("Create the following Dancer?\n\n")
    new_dnc.print_full_data()
    if IPT_getBool("Confirm Creation (y/n)"):
        new_dnc.save()
        return new_dnc
    else:
        print("Deleting Dancer, starting over")
        return create_new_Dancer()


def alter_existing_Dancer() -> Dancer:
    dnc_id, _ = IPT_await(msg="Enter Dancer Id: ")
    dnc = loadDancer(dnc_id)
    if not dnc:
        return create_new_Dancer(dnc_id)
    print("Selected Dancer:")
    dnc.print_full_data()
    while True:
        cmd = IPT_command(["name", "gender", "done"], msg="What to change? (name, gender)")
        match cmd:
            case "name":
                dnc._name = input("Enter new Name: ")
                print("Enter 'done' to finish editing")
            case "gender":
                dnc._gender = IPT_command(["b", "g", "b/g"], msg="Enter new Gender (b, g, b/g): ")
                print("Enter 'done' to finish editing")
            case "done":
                dnc.save()
                return dnc


def get_full_data():
    dnc = loadDancer(IPT_await()[0])
    dnc.print_full_data()


def load_data_base() -> list[Dancer]:
    """
    Loads all dancer files from the `./dnc` directory that have the `.dnc` extension.

    :return: A list of `Dancer` objects parsed from the `.dnc` files in the `./dnc` directory
    :rtype: list[Dancer]
    """
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


def sort_list_by_last_danced(lst: list[Dancer]) -> list[Dancer]:
    rtn = []
    while lst:
        minD = min(lst, key=lambda x: x.getLastDanced())
        mini = minD.getLastDanced()
        tmp = []
        for i, dnc in enumerate(lst):
            if dnc.getLastDanced() == mini:
                tmp.append(dnc)
        for dnc in tmp:
            lst.remove(dnc)
        rtn += sort_list_by_danced_factor(tmp)
    return rtn




def sort_list_by_danced_factor(lst: list[Dancer]) -> list[Dancer]:
    frac_lst = []
    for dnc in lst:
        frac_lst.append(dnc.getDancedFactor())
    return reorder_list_by_index_permutation(lst, FRAC_sort_list_to_permutation(frac_lst))
    """
    return rtn
    """

    """
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
                continue
    return rtn
    """


def sort_list_by_name(lst: list[Dancer]) -> list[Dancer]:
    return sorted(lst, key=lambda x: x.getName())


def reorder_list_by_index_permutation(lst: list[object], idx_lst: list[int]) -> list[object]:
    if len(lst) != len(idx_lst):
        raise ValueError
    rtn = []
    for idx in idx_lst:
        rtn.append(lst[idx])
    return rtn


def shuffle_list(lst: list[object]) -> list[object]:
    import random
    rtn = []
    while lst:
        rtn.append(lst.pop(random.randint(0, len(lst) - 1)))
    return rtn


if __name__ == "__main__":
    for dancer in get_present_dancers(sort_list_by_last_danced(load_data_base())):
        print(dancer)

    create_new_Dancer(370452)
