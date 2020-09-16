#IsVowel?py     03.02.2020

#program #6

#Get the word(s)
print("please enter a word:")
ourInput = input().lower()
#set the output
output = ""
vowels = ["a", "e", "i", "o", "u"]
digits = [str(i) for i in range(0, 10)]

#iterate through the string
for ourChar in ourInput:
    if ourChar == " ":
        output += "Space, "
    if ourChar in vowels:
        output += "Vowel, "
    if ourChar in digits:
        output += "Digit, "
    if ourChar != " " and ourChar not in vowels and ourChar not in digits:
        output += "Consonant, "
    
print(output)