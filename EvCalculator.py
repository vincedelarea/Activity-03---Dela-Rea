from sympy import *
import main as mainFile

class compEV:
     #Int rstat, Float Modif, Int Level, Int Base, Int IV, Int EV, Int Nature
    def EVCalc(rStat, rModif, rLevel, rBase, rIV, rEV, rNature):
        statVal = {
            "Stat": 100,
            "Modifiers": 1.0,
            "Level": 100,
            "Base": 120,
            "IV": 10,
            "EV": 50,
            "Nature": 1
        }

        stat, mod, d, lvl, base, iv, ev = symbols("stat, mod, d, lvl, base, iv, ev")
        formulaD = ((2*base+iv+(ev/4))*lvl/100)
        formulaEV = (((((stat/mod)-d)*400)/lvl)/4)*4
        D = N(formulaD.subs([(base,statVal["Stat"]),(iv,statVal["IV"]),(ev,statVal["EV"]),(lvl,statVal["Level"])]))
        EV = round(N(formulaEV.subs([(stat,statVal["Stat"]),(mod,statVal["Modifiers"]),(d,D),(lvl,statVal["Level"])])))
        print(D)
        print(EV)
        
compEV.EVCalc()