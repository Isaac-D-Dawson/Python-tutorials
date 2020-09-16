#PressureKilopascalsTo.py       04.02.2020

#program #11

#get the input and set up enviroment variables
print("Please enter the pressure in kilopascals:")
kiloPascals = int(input())
poundsSquareInch = kiloPascals * 0.145038
milimiterMercury = kiloPascals * 7.50062
atmosphericPressue = kiloPascals * 0.00986923

print(f"{kiloPascals} in KiloPascals is equal to:")
print(f"{poundsSquareInch} Pouds per Square Inch")
print(f"{milimiterMercury} Milimetres of Mercury")
print(f"{atmosphericPressue} times earths atmospheric pressure")