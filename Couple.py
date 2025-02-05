from random import randint

from Dancer import *

class Couple:
    def __init__(self, boy: Dancer, girl: Dancer):
        self.boy = boy
        self.girl = girl
    

    def __str__(self):
        rtn = ""
        rtn += f"{self.boy:<15} | {self.girl:>15}"
        return rtn

    def save(self):
        self.boy.save()
        self.girl.save()

def TEST_get_test_Couples(amount: int)->list[Couple]:
    rtn = []

    for i in range(amount):
        dnc1 = loadDancer(f"00000{randint(1, 9)}")
        dnc2 = loadDancer(f"00000{randint(1, 9)}")
        rtn += [Couple(dnc1, dnc2)]

    return rtn




if __name__ == "__main__":
    dn1 = loadDancer(123456)
    print(Couple(dn1, dn1))
        