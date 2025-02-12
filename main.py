from func import *
from Dancer import *
from Rotate import *

MAIN_SPECIALS = ["exit", "start", "print", "reset", "reload", "details", "new"]
rt: Rotate = Rotate()


def handle_specials(word):
    match word:
        case "exit":
            exit(0)
        case "start":
            sLst = rt.newRound()
            for square in sLst:
                print(square)
        case "print":
            print(rt)
        case "reset":
            rt.resetDancers()
        case "reload":
            rt.reloadLists()
        case "details":
            id, _ = IPT_await()
            dnc = loadDancer(id)
            dnc.print_full_data()
        case "new":
            dnc = create_new_Dancer()
            dnc.save()
            print(f"Created {dnc:+g}")




def main():
    rt.reloadLists()
    while True:
        ipt, isSpecial = IPT_await(MAIN_SPECIALS)
        if isSpecial:
            handle_specials(ipt)
        else:
            rt.pauseDancer(ipt, sendLog=True)



if __name__ == '__main__':
    main()
