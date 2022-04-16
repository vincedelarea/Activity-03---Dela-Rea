from sympy import *

class compEV:
     #Int rstat, Float Modif, Int Level, Int Base, Int IV, Int EV, stat
    def EVCalc(rStat, rModif, rLevel, rBase, rIV, rEV, stat):
        nature = rModif
        natureMod = 1
        if(stat=="HP"):
            natureMod = 1
        elif(stat=="Sp.Def"):
            if(nature>=20 and nature<=23):
                natureMod = 1.1
            elif(nature==4 or nature==9 or nature==14 or nature==19):
                natureMod = 0.9
            else:
                natureMod = 1
        elif(stat=="Sp.Atk"):
            if(nature>=15 and nature<=19):
                natureMod = 1.1
            elif(nature==3 or nature==8 or nature==13 or nature==23):
                natureMod = 0.9
            else:
                natureMod = 1
        elif(stat=="Speed"):
            if(nature>=10 and nature<=14):
                natureMod = 1.1
            elif(nature==2 or nature==7 or nature==17 or nature==22):
                natureMod = 0.9
            else:
                natureMod = 1
        elif(stat=="Defense"):
            if(nature>=5 and nature<=9):
                natureMod = 1.1
            elif(nature==1 or nature==11 or nature==16 or nature==21):
                natureMod = 0.9
            else:
                natureMod = 1
        elif(stat=="Attack"):
            if(nature>=1 and nature<=4):
                natureMod = 1.1
            elif(nature==5 or nature==10 or nature==15 or nature==20):
                natureMod = 0.9
            else:
                natureMod = 1
        statVal = {
            "Stat": rStat,
            "Modifiers": natureMod,
            "Level": rLevel,
            "Base": rBase,
            "IV": rIV,
            "EV": rEV
        }

        stat, mod, d, lvl, base, iv, ev = symbols("stat, mod, d, lvl, base, iv, ev")
        formulaD = ((2*base+iv+(ev/4))*lvl/100)
        formulaEV = (((((stat/mod)-d)*400)/lvl)/4)*4
        D = N(formulaD.subs([(base,statVal["Stat"]),(iv,statVal["IV"]),(ev,statVal["EV"]),(lvl,statVal["Level"])]))
        EV = round(N(formulaEV.subs([(stat,statVal["Stat"]),(mod,statVal["Modifiers"]),(d,D),(lvl,statVal["Level"])])))
        return(EV)
        