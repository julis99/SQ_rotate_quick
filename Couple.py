from Dancer import *

class Couple:
    def __init__(self, boy: Dancer, girl: Dancer):
        self.boy = boy
        self.girl = girl
    

    def __str__(self):
        rtn = ""
        rtn += f"{self.boy:<15} | {self.girl:>15}"
        return rtn




if __name__ == "__main__":
    dn1 = loadDancer(123456)
    print(Couple(dn1, dn1))
        