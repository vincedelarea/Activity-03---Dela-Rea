from sympy import *
import StatCalculator as StatCalc
import EvCalculator as EvCalc

num = 0
global baseHP, baseSDef, baseSAtk,  baseSpeed, baseDef, baseAtk

#BOOLEAN T single or F all stats
def getStats(count, statnum):
    if(count==True):
        if(statnum==1):
            baseHP = input("Base HP:")
        elif(statnum==2):
            baseSDef = input("Base Sp.Def:")
        elif(statnum==3):
            baseSAtk = input("Base Sp.Atk:")
        elif(statnum==4):
            baseSpeed = input("Base Speed:")
        elif(statnum==5):
            baseDef = input("Base Defense:")
        elif(statnum==6):
            baseAtk = input("Base Attack:")
        else:
            ("Invalid Choice.")    
    elif(count==False):
        baseHP = input("Base HP:")
        baseSDef = input("Base Sp.Def:")
        baseSAtk = input("Base Sp.Atk:")
        baseSpeed = input("Base Speed:")
        baseDef = input("Base Defense:")
        baseAtk = input("Base Attack:")
    StatCalc.compStats.setStats(baseHP, baseSDef, baseSAtk, baseSpeed, baseDef, baseAtk)
    
    
while(True):
    num = int(input("1. Compute Stat\n2. Compute EV\n3. Exit\nEnter number:"))
    if(num>=1 and num<=3):
        if(num==1):
            num = int(input("1. Compute single stat\n2. Compute all stats\nEnter number:"))
            if(num==1):
                num = input("""1. HP       2. Sp.Def       3. Sp.Atk
                4. Speed    5. Defense      6. Attack
                Enter Number:""")
                getStats(True, num)
            elif(num==2):
                getStats(False, None)
        elif(num==2):
            num=input("1. Calculate single stat\n2.Calculate all stat\nEnter number:")
            EvCalc.EvCalcSingleStat()
            continue
        else:
            print("Exiting Program")
            break
    else:
        print("Error input")

