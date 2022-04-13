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
def getStats():
    global level, IV, nature, baseHP, baseSDef, baseSAtk,  baseSpd, baseDef, baseAtk
    global ivHP, evHP, ivSDef, evSDef, ivSAtk, evSAtk, ivSpd, evSpd, ivDef, evDef, ivAtk, evAtk
    while(True):
        level = int(input("Pokemon level:"))
        IV = int(input("Value should be (0-31)\nPokemon IV:"))
        nature = int(input("""
    0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
    1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
    2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
    3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
    4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky
    Enter number:"""))
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
        elif(num==2):
            num=input("1. Calculate single stat\n2.Calculate all stat\nEnter number:")
            EvCalc.EvCalcSingleStat()
            continue
        else:
            print("Exiting Program")
            break
    else:
        print("Error input")
    # StatCalc.compStats.setStats(baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk)