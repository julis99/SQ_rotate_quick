from Rotate import *
from func import *


def EVAL_present_genders(prints: bool = False) -> tuple[int, int, int]:
    """
    Evaluates and counts the genders of present dancers in the loaded database.

    This function reads data from a loaded database and counts the number of boys,
    girls, and those who identify as both genders among the present dancers. It
    also optionally prints a formatted summary of the counts and their respective
    proportions if the `prints` parameter is set to True. This evaluation assumes
    the presence of dancers to be determined by a `is_present` method and their
    gender to be retrieved using a `getGender` method from the provided data.

    :param prints: If set to True, outputs a formatted representation of the
        results. Defaults to False.
    :type prints: bool

    :return: A tuple containing the following:
        - The count of boys present.
        - The count of girls present.
        - The count of those identifying as both genders present.
    :rtype: tuple[int, int, int]
    """
    lst = load_data_base()
    numBoys = 0
    numGirls = 0
    numBoth = 0
    for dnc in lst:
        if dnc.is_present():
            if dnc.getGender() == "b":
                numBoys += 1
            elif dnc.getGender() == "g":
                numGirls += 1
            elif dnc.getGender() == "b/g":
                numBoth += 1
            else:
                raise ValueError
    if prints:
        print(r"###############################EVAL###############################")
        print(r"          Present Dancer Genders")
        print(r"##################################################################")
        print(f"   BOYS : {numBoys}, {(numBoys / (numGirls + numBoth + numBoys)) * 100} %")
        print(f"   GIRLS: {numGirls}, {(numGirls / (numGirls + numBoth + numBoys)) * 100} %")
        print(f"   BOTH : {numBoth}, {(numBoth / (numGirls + numBoth + numBoys)) * 100} %")
        print(r"##############################ENDEVAL#############################")
    return numBoys, numGirls, numBoth


def EVAL_dancers_danced(prints: bool = False) -> {int, int}:
    """
    Evaluate the minimum and maximum number of dances performed by dancers in the database.

    This function retrieves data about dancers from the database, determines the minimum
    and maximum number of dances performed by any dancer in the dataset, and optionally
    prints debugging information.

    :param prints: Optional; indicates whether to print debugging information to the
                   console. Defaults to False.
    :type prints: bool
    :return: A list containing the minimum and maximum number of dances performed by
             dancers. The first element represents the minimum and the second element
             represents the maximum.
    :rtype: list[int]
    """
    lst = load_data_base()
    mini = Fraction(1, 1)
    maxi = Fraction(0, 1)
    zero = Fraction(0, 0)
    for dnc in lst:
        if dnc.getDancedFactor() == zero:
            continue
        if dnc.getDancedFactor() < mini:
            mini = dnc.getDancedFactor()
        if dnc.getDancedFactor() > maxi:
            maxi = dnc.getDancedFactor()
    if prints:
        lst = sort_list_by_last_danced(lst)
        print(r"###############################EVAL###############################")
        print(r"                      Dancer Participation")
        print(r"##################################################################")
        print(f" Minimum of particpations: {mini}")
        print(f" Maximum of particpations: {maxi}")
        print(f" Difference in NUM       : {maxi.numerator - mini.numerator}")
        print(r"##################################################################")
        print(r" Dancers:")
        lst = sort_list_by_danced_factor(lst)
        for dnc in lst:
            if dnc.getDancedFactor() == zero:
                continue
            print(f"    {dnc:+a}")
        print(r"##############################ENDEVAL#############################")
    return [mini, maxi]


def TEST_test_rotation(runs: int):
    rt = Rotate()
    rt.reloadLists()
    rt.resetDancers()
    print(r"###############################TEST###############################")
    print(r"##################################################################")
    print(f" Performing {runs} rounds with {rt.possibleSquares} possible squares each")
    EVAL_present_genders(True)
    for i in range(runs):
        rt.newRound()
    EVAL_dancers_danced(True)
    print(r"##################################################################")
    print(r"##############################ENDTEST#############################")


if __name__ == "__main__":
    TEST_test_rotation(100)
