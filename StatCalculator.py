from sympy import *

class compStats:

    # def __init__(baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk):
    #     self.baseHP = 1
    baseHP=baseSDef=baseSAtk=baseSpeed=baseDef=baseAtk = 0

    def setStats(bHP, bSDef, bSAtk, bSpeed, bDef, bAtk):
        baseHP=bHP
        baseSDef=bSDef
        baseSAtk=bSAtk
        baseSpeed=bSpeed
        baseDef=bDef
        baseAtk=bAtk

    
    def StatMain():
        return 0

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

    
    def OtherStat(base, iv, ev, lvl, nature):
        statval = {
            "Base": base,
            "IV": iv,
            "EV": ev,
            "Level": lvl,
            "Nature": nature
        }
        base, iv, ev, lvl, nat = symbols("base, iv, ev, lvl, nat")
        stat = (((((2*base+iv+(ev/4))*lvl)/100)+5)*nat)
        return stat

#baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk