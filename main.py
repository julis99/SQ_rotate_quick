from func import *
from Dancer import *
from Rotate import *

MAIN_SPECIALS = ["exit", "start", "print", "reset"]
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


def main():
    rt.reloadlists()
    while True:
        ipt, isSpecial = IPT_await(MAIN_SPECIALS)
        if isSpecial:
            handle_specials(ipt)
        else:
            dnc = loadDancer(ipt)
            dnc.print_full_data()


if __name__ == '__main__':
    main()
