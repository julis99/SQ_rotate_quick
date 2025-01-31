from Dancer import *

def IPT_await(specials=[]) -> [str, bool]:
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

