from sympy import *

class compStats:

    def StatMain():
        print()

    def HpStat():
        statval = {
            "Base": 20,
            #0-31
            "IV": 31,
            #0-255
            "EV": 255,
            "Level": 100
        }
        hpval = 0
        base, iv, ev, lvl = symbols("base, iv, ev, lvl")
        hp = (((2*base+iv+(ev/4)*lvl)/100)+lvl+10)
        hpval = round(N(hp.subs([(base, statval["Base"]),(iv, statval["IV"]),(ev,statval["EV"]),(lvl,statval["Level"])])))
        return hpval

    def OtherStat():
        statval = {
            "Base": 0,
            "IV": 0,
            "EV": 0,
            "Level": 0,
            "Nature": 0
        }
        base, iv, ev, lvl, nat = symbols("base, iv, ev, lvl, nat")
        stat = (((((2*base+iv+(ev/4))*lvl)/100)+5)*nat)


print(compStats.HpStat())