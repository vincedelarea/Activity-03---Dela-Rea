from shutil import which
from sympy import *
import os
import StatCalculator as StatCalc
import EvCalculator as EvCalc

num = 0

evHP=0
evSDef=0
evSAtk=0
evSpd=0
evDef=0
evAtk=0
#BOOLEAN T single or F all stats
#count, statnum

chstat = """
1. HP        2. Sp.Def       3. Sp.Atk        
4. Speed     5. Defense      6. Attack
Enter number:"""

printNature = """
0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky
Enter number:"""
#Boolean TRUE if single stat otherwise false,
def evGet(val, stat):
    EVIncrease = 0
    # 0:HP, 1:Sp.Def, 2:Sp.Atk, 3:Speed, 4:Def, 5:Atk
    StatIncrease = [0, 0, 0, 0, 0, 0]
    nature = 0
    if(num!=1):
        nature = int(input(printNature))
    level = int(input("Level:"))
    IV = int(input("Value should be (0-31)\nPokemon IV:"))
    if(val==True):
        EVIncrease = int(input("Increase in stat:"))
        if(stat==1):
            baseHP = int(input("Base HP:"))
            evHP = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseHP, IV, evHP, "HP"))
        elif(stat==2):
            baseSDef = int(input("Base Sp.Def:"))
            evSDef = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseSDef, IV, evSDef, "Sp.Def"))
        elif(stat==3):
            baseSAtk = int(input("Base Sp.Atk:"))
            evSAtk = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseSAtk, IV, evSAtk, "Sp.Atk"))
        elif(stat==4):
            baseSpd = int(input("Base Speed:"))
            evSpd = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseSpd, IV, evSpd, "Speed"))
        elif(stat==5):
            baseDef = int(input("Base Defense:"))
            evDef = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseDef, IV, evDef, "Defense"))
        elif(stat==6):
            baseAtk = int(input("Base Attack:"))
            evAtk = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
            print(EvCalc.compEV.EVCalc(EVIncrease, nature, level, baseAtk, IV, evAtk, "Attack"))
        input("")
    elif(val==False):
        baseHP = int(input("Base HP:"))
        evHP = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[0] = int(input("Increase in stat:"))
        baseSDef = int(input("Base Sp.Def:"))
        evSDef = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[1] = int(input("Increase in stat:"))
        baseSAtk = int(input("Base Sp.Atk:"))
        evSAtk = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[2] = int(input("Increase in stat:"))
        baseSpd = int(input("Base Speed:"))
        evSpd = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[3] = int(input("Increase in stat:"))
        baseDef = int(input("Base Defense:"))
        evDef = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[4] = int(input("Increase in stat:"))
        baseAtk = int(input("Base Attack:"))
        evAtk = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nCurrent EV:"))
        StatIncrease[5] = int(input("Increase in stat:"))
        #Int rstat, Float Modif, Int Level, Int Base, Int IV, Int EV, STAT
        print("EVs need to increase stats:")
        print("HP:", EvCalc.compEV.EVCalc(StatIncrease[0], nature, level, baseHP, IV, evHP, ""))
        print("Sp.Def:", EvCalc.compEV.EVCalc(StatIncrease[1], nature, level, baseSpd, IV, evSDef, ""))
        print("Sp.Atk:", EvCalc.compEV.EVCalc(StatIncrease[2], nature, level, baseSAtk, IV, evSAtk, ""))
        print("Speed:", EvCalc.compEV.EVCalc(StatIncrease[3], nature, level, baseSpd, IV, evSpd, ""))
        print("Defense:", EvCalc.compEV.EVCalc(StatIncrease[4], nature, level, baseDef, IV, evDef, ""))
        print("Attack:", EvCalc.compEV.EVCalc(StatIncrease[5], nature, level, baseAtk, IV, evAtk, ""))
        input("")

        

def getStats():
    global level, IV, nature, baseHP, baseSDef, baseSAtk,  baseSpd, baseDef, baseAtk
    global ivHP, evHP, ivSDef, evSDef, ivSAtk, evSAtk, ivSpd, evSpd, ivDef, evDef, ivAtk, evAtk
    while(True):
        level = int(input("Pokemon level:"))
        IV = int(input("Value should be (0-31)\nPokemon IV:"))
        nature = int(input(printNature))
        baseHP = int(input("Base HP:"))
        evHP = int(input("Value should be (0-255) Max EV value of all stat should not exceed 510\nEV:"))
        maxEv = evHP
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            continue
        baseSDef = input("Base Sp.Def:")
        evSDef = int(input("EV:"))
        maxEv = evHP+evSDef
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            continue
        baseSAtk = input("Base Sp.Atk:")
        evSAtk = int(input("EV:"))
        maxEv = evHP+evSDef+evSAtk
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            continue
        baseSpd = input("Base Speed:")
        evSpd = int(input("EV:"))
        maxEv = evHP+evSDef+evSAtk+evSpd
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            continue
        baseDef = input("Base Defense:")
        evDef = int(input("EV:"))
        maxEv = evHP+evSDef+evSAtk+evSpd+evDef
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            continue
        baseAtk = input("Base Attack:")
        evAtk = int(input("EV:"))
        maxEv = evHP+evSDef+evSAtk+evSpd+evDef+evAtk
        if(maxEv>510):
            print("Total Stat EV should not exceed 510.")
            input("")
            continue
        break

def printStats():
    print("HP:", StatCalc.compStats.HpStat(baseHP, IV, evHP, level))
    print("Sp.Def:", StatCalc.compStats.OtherStat(baseSDef, IV, evSDef, level, "Sp.Def", nature))
    print("Sp.Atk:", StatCalc.compStats.OtherStat(baseSAtk, IV, evSAtk, level, "Sp.Atk", nature))
    print("Speed:", StatCalc.compStats.OtherStat(baseSpd, IV, evSpd, level, "Speed", nature))
    print("Defense:", StatCalc.compStats.OtherStat(baseDef, IV, evDef, level, "Defense", nature))
    print("Attack:", StatCalc.compStats.OtherStat(baseAtk, IV, evAtk, level, "Attack", nature))
    input("")


while(True):
    num = int(input("1. Compute Stat\n2. Compute EV\n3. Exit\nEnter number:"))
    if(num>=1 and num<=3):
        if(num==1):
            getStats()
            printStats()
        elif(num==2):
            num=int(input("1. Calculate single stat\n2. Calculate all stat\nEnter number:"))
            if(num==1):
                num=int(input(chstat))
                evGet(True, num)
            elif(num==2):
                evGet(False, 0)
            continue
        else:
            print("Exiting Program")
            break
    else:
        print("Error input")
    # StatCalc.compStats.setStats(baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk)