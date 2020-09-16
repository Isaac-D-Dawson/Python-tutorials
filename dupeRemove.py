#dupeRemove.py      04.02.2020

#Program 9

#Get out list with duplicates.
startList = "1,1,2,2,3,3,4,5,6,6,7,8,9,9,9,9".split(",")
#make a set out of it.
startSet = set(startList)
#Re-list and sort the set.
#print(sorted(list(startSet)))
endList = list(startSet)
endList.sort()
print(endList)