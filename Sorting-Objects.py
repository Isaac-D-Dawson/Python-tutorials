#Storing objects    26.11.2019

li = [9, 2, 5, -4, 3, 2, -6, -3, 2, -8, -9, 9]

s_li = sorted(li)

#print(s_li)
#print(sorted("Hello and again...", reverse=True))

#sorted() returns a sorted list.
#.sort() overwistes the original list.
# "reverse=True" allows the string to exit reversed.
#.sort only works on lists.

ks_li = sorted(li, key=abs)
print(ks_li)
print(abs(li[0]))

#The "key=" paramiter runs each item in the list through
# the function and then sorts according to the result, lowest ouput to highest out.
#This works for any function, within reason.
#Doesnt work with methods?

# #Proof of concept code for "run with any function".
# loop = 0

# def oddsort(in_item):
#     global loop
#     loop = loop+1
#     return loop - in_item
    
# t_li = [1, 3, 2, 9]
# kst_li = sorted(t_li, key=oddsort)
# print(kst_li)

#print(t_li.index(9))