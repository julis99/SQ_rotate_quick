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
        print(r"")
        print(f"  Total : {numGirls + numBoth + numBoys}")
        print(r"##############################ENDEVAL#############################")
    return numBoys, numGirls, numBoth


def EVAL_dancers_danced(prints: bool = False) -> tuple[Fraction, Fraction, int, int]:
    """
    Evaluates dancers' participation and their danced factors based on the given data.

    This function analyzes the list of dancers and computes various metrics such as
    the minimum and maximum participation factors, the difference in the numerator,
    the smallest and largest denominators, and displays relevant statistics if
    requested. It returns a tuple containing the minimum factor, maximum factor,
    and the maximum difference in the denominator.

    :param prints: A boolean flag. If True, prints a detailed evaluation of
        dancer participation and factors. If False, only computes and returns
        the metrics.
    :return: A tuple containing three integers:
        - minimum danced factor,
        - maximum danced factor,
        - maximum difference in participation denominators.
    """
    lst = load_data_base()
    mini = Fraction(1, 1)
    maxi = Fraction(0, 1)
    max_diff = 0
    min_diff = float('inf')
    min_denom = float('inf')
    max_denom = 0
    zero = Fraction(0, 0)
    for dnc in lst:
        factor = dnc.getDancedFactor()
        if factor == zero:
            continue
        if factor < mini:
            mini = factor
        if factor > maxi:
            maxi = factor
        max_diff = max(max_diff, factor.denominator - factor.numerator)
        min_diff = min(min_diff, factor.denominator - factor.numerator)
        min_denom = min(min_denom, factor.denominator)
        max_denom = max(max_denom, factor.denominator)

    if prints:
        lst = sort_list_by_last_danced(lst)
        print(r"###############################EVAL###############################")
        print(r"                      Dancer Participation")
        print(r"##################################################################")
        print(f" Minimum of particpations: {mini}")
        print(f" Maximum of particpations: {maxi}")
        print(f" Minimum of forced breaks: {min_diff}")
        print(f" Maximum of forced breaks: {max_diff}")
        print(r"##################################################################")
        print(r"                         Dancer Factors")
        print(r"##################################################################")
        print(f" Minimum denominator overall: {min_denom}")
        print(f" Maximum denominator overall: {max_denom}")

        print(r" Dancers:")
        lst = sort_list_by_danced_factor(lst)
        for dnc in lst:
            if dnc.getDancedFactor() == zero:
                continue
            print(f"    {dnc:+a}")
        print(r"##############################ENDEVAL#############################")
    return [mini, maxi, min_diff, max_diff]


def TEST_test_rotation(runs: int, withPausing: bool = False):
    rt = Rotate()
    rt.reloadLists()
    rt.resetDancers()
    print(r"###############################TEST###############################")
    print(r"##################################################################")
    print(f" Performing {runs} rounds with {rt.possibleSquares} possible squares each")
    if withPausing:
        print(r"  with pausing Dancers")
    else:
        print(r"  without pausing Dancers")
    EVAL_present_genders(True)
    for i in range(runs):
        rt.newRound()
        if withPausing:
            rdm = random.randint(0, rt.getNumPresent() // 4)
            for j in range(rdm):
                rIdx = random.randint(0, rt.getNumAvailable() - 1)
                rt.pauseDancer(rt._avaible[rIdx].getId())
    EVAL_dancers_danced(True)
    print(r"##################################################################")
    print(r"##############################ENDTEST#############################")


if __name__ == "__main__":
    TEST_test_rotation(100, True)
    #EVAL_dancers_danced(True)
