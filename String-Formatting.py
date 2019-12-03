#String-formatting.py   03.12.2019

# #use of f-strings
# for i in range(1, 11):
#     sentence = f"The value is {i:02}"
#     print(sentence)

# #The :02 operator ensures that there are a total of 2 digits,
# # and pads the remainder with "0"s.
# #Using non-zero numbers adds more spaces between.

# #Rounding using formatted strings

pi = 3.14159265

# print(f"Pi is equal to {pi:.4f}")
# print(f"Pi is equal to {pi:.5}")
# #Note that suffixing with an f changes it to mesure decimal places rather than significant figures.


#print(f"1MN is wuqal to {1000**2:,} bytes")

#Commas can be used to seperate different functions applying to the same format.
print(f"Pi is equal to {pi:06,.4}")
#Note that these have to be done in the right order. eg:
#print(f"Pi is equal to {pi:.4, 06}") #Throws an error