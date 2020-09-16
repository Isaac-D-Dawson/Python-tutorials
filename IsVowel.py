#IsVowel?py     03.02.2020

#program #6

print("please enter a letter:")
ourInput = input().lower()
#To make sure we only get one letter
ourChar = ourInput[0]
if ourChar in ["a", "e", "i", "o", "u"]:
    print("Your letter is a vowel!")
else:
    print("Your letter is not a vowel")