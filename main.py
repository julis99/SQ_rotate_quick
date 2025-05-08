import os
from Rotate import *

MAIN_SPECIALS = ["exit", "start", "print", "reset", "reload", "details", "new", "alter", "logout", "manipulate", "help"]
MAIN_HELP = ("SQ - ROTATE - QUICK\n"
             "Help Menu\n"
             "Enter your Barcode to become pausing, away, or available again\n"
             "Or Enter a special keyword:\n"
             " - exit       - Exits this program (Warning: This will lose track of any pausing dancers)\n"
             " - start      - Starts a new round\n"
             " - print      - Prints all registered Dancers (split into available, pausing and away)\n"
             " - reset      - Resets the num Danced for all registered Dancers\n"
             " - reload     - Reloads the registered Dancers into the Rotation\n"
             " - details    - Get Details for a specific Dancer\n"
             " - new        - Register a new Dancer (Discards Pausing)\n"
             " - alter      - Alter a already registered Dancer (or create new Dancer if ID unknown) (Discards Pausing)\n"
             " - logout     - Makes every Dancer be away\n"
             " - manipulate - Manipulate the current round\n"
             " - help       - Shows this menu")

MAIN_WELCOME = r""" ____   ___      ____   ___ _____  _  _____ _____     ___  _   _ ___ ____ _  __
/ ___| / _ \    |  _ \ / _ \_   _|/ \|_   _| ____|   / _ \| | | |_ _/ ___| |/ /
\___ \| | | |   | |_) | | | || | / _ \ | | |  _|    | | | | | | || | |   | ' / 
 ___) | |_| |   |  _ <| |_| || |/ ___ \| | | |___   | |_| | |_| || | |___| . \ 
|____/ \__\_\___|_| \_\\___/ |_/_/   \_\_| |_____|___\__\_\\___/|___\____|_|\_\
           |_____|                              |_____|                         """

rt: Rotate = Rotate()


def MAIN_handle_specials(word):
    match word:
        case "exit":
            exit(0)
        case "start":
            if not MAIN_new_round():
                print(rt)
        case "print":
            print(rt)
        case "reset":
            rt.resetDancers()
        case "reload":
            rt.reloadLists()
        case "details":
            id, isSpecial = IPT_await(["all"], "Scan Id or type 'all': ")
            if isSpecial:
                print(rt.detailed())
                return
            dnc = loadDancer(id)
            if dnc:
                dnc.print_full_data()
            else:
                print("\n\n")
        case "new":
            dnc = create_new_Dancer()
            dnc.save()
            print(f"Created {dnc:+g}")
            rt.reloadLists()
        case "alter":
            dnc = alter_existing_Dancer()
            dnc.save()
            print(f"Altered {dnc}")
            rt.reloadLists()
        case "logout":
            rt.clearAvailable()
        case "manipulate":
            rd, _ = IPT_await(msg="Enter Round Number: ")
            rt.manipulate(int(rd))
        case "help":
            print(MAIN_HELP)
        case _:
            print(MAIN_HELP)


def MAIN_new_round() -> bool:
    sLst = rt.newRound()
    if not sLst:
        print("No Squares possible, please adjust Dancers\n"
              "Printing all registered Dancers...\n\n")
        return False
    for square in sLst:
        print(square)
    return True


def main():
    rt.reloadLists()
    print(MAIN_WELCOME)
    while True:
        ipt, isSpecial = IPT_await(MAIN_SPECIALS, msg="Scan Barcode or Enter Command (help for more info):  ")
        if isSpecial:
            MAIN_handle_specials(ipt)
        else:
            if existDancer(ipt):
                rt.pauseDancer(ipt, sendLog=True)
            else:
                print(f"No Dancer with id [{ipt}] found")
                if IPT_getBool("Create new Dancer? (y/n)"):
                    dnc = create_new_Dancer(ipt)
                    dnc.save()
                    rt.reloadLists()
                else:
                    print("Dancer not created")

            


if __name__ == '__main__':
    main()
