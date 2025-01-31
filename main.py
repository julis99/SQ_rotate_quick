from func import *
from Dancer import *


def main():
    dnc = Dancer()
    did, bl = IPT_await()
    dnc = loadDancer(did)
    dnc.print_full_data()
    dnc.switch_presence()
    dnc.print_full_data()
    dnc.save()


if __name__ == '__main__':
    main()
