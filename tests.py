from Rotate import *
from func import *


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
    for dnc in lst:
        if dnc.getDancedFactor() < mini:
            mini = dnc.getDancedFactor()
        if dnc.getDancedFactor() > maxi:
            maxi = dnc.getDancedFactor()
    if prints:
        lst = sort_list_by_num_danced(lst)
        print(r"##############################EVAL##############################")
        print(r"                      Dancer Participation")
        print(r"##################################################################")
        print(f" Minimum of particpations: {mini}")
        print(f" Maximum of particpations: {maxi}")
        print(r"##################################################################")
        print(r" Dancers:")
        for dnc in lst:
            print(f"    {dnc:+n}")
    return [mini, maxi]


if __name__ == "__main__":
    EVAL_dancers_danced(True)
