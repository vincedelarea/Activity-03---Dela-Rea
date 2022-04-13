from sympy import *

class compStats:

    def HpStat(base, iv, ev, lvl):
        statval = {
            "Base": base,
            #0-31
            "IV": iv,
            #0-255
            "EV": ev,
            "Level": lvl
        }
        hpval = 0
        base, iv, ev, lvl = symbols("base, iv, ev, lvl")
        hp = (((2*base+iv+(ev/4)*lvl)/100)+lvl+10)
        hpval = round(N(hp.subs([(base, statval["Base"]),(iv, statval["IV"]),(ev,statval["EV"]),(lvl,statval["Level"])])))
        return hpval

    def OtherStat(base, iv, ev, lvl, stat, nature):
        natureMod = 0
        if(stat=="Sp.Def"):
            if(nature>=20 and nature<=23):
                natureMod = 1.1
            elif(nature==4 or nature==9 or nature==14 or nature==19):
                natureMod = 0.9
            else:
                natureMod = 1
        if(stat=="Sp.Atk"):
            if(nature>=15 and nature<=19):
                natureMod = 1.1
            elif(nature==3 or nature==8 or nature==13 or nature==23):
                natureMod = 0.9
            else:
                natureMod = 1
        if(stat=="Speed"):
            if(nature>=10 and nature<=14):
                natureMod = 1.1
            elif(nature==2 or nature==7 or nature==17 or nature==22):
                natureMod = 0.9
            else:
                natureMod = 1
        if(stat=="Defense"):
            if(nature>=5 and nature<=9):
                natureMod = 1.1
            elif(nature==1 or nature==11 or nature==16 or nature==21):
                natureMod = 0.9
            else:
                natureMod = 1
        if(stat=="Attack"):
            if(nature>=1 and nature<=4):
                natureMod = 1.1
            elif(nature==5 or nature==10 or nature==15 or nature==20):
                natureMod = 0.9
            else:
                natureMod = 1
        statval = {
            "Base": base,
            "IV": iv,
            "EV": ev,
            "Level": lvl,
            "Nature": natureMod
        }
        base, iv, ev, lvl, nat = symbols("base, iv, ev, lvl, nat")
        stat = (((((2*base+iv+(ev/4))*lvl)/100)+5)*nat)
        statval = N(stat.subs([(base,statval["Base"]),(iv,statval["IV"]),(ev,statval["EV"]),(lvl,statval["Level"]),(nat,statval["Nature"])])).evalf(4)
        return statval

#baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk