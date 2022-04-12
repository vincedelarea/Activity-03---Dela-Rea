from sympy import *
import StatCalculator as StatCalc
import EvCalculator as EvCalc

num = 0

while(True):
    num = int(input("1. Compute Stat\n2. Compute EV\n3. Exit\nEnter number:"))
    if(num>=1 and num<=3):
        if(num==1):
            StatCalc.StatCompute()
            continue
        elif(num==2):
            num=input("1. Calculate single stat\n2.Calculate all stat\nEnter number:")
            EvCalc.EvCalcSingleStat()
            continue
        else:
            print("Exiting Program")
            break
    else:
        print("Error input")

