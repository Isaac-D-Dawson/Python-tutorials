#f-string-formatting.py     03.03.2020

firstName = "isaac"
lastName = "d. dawson"

# sentence = "My name is {} {}.".format(firstName, lastName)
sentence = f"My name is {firstName.upper()} {lastName.upper()}."
print(sentence)
#f strings allow for direct inserts of function or variables into strings.
#Like the .format() method, fstrings are generally more readale.

person = {"name": "Dave", "age": "15"}
#sentence = "My name is {} and I'm {} years old.".format(person["name"], person["age"])
#sentence = f"My name is {person["name"]} and I'm {person["age"]} years old." #Will return a syntax error
sentence = f"My name is {person['name']} and I'm {person['age']} years old."
print(sentence)
#Note that while using strings inside of .format is perfectly fine(Here we used them as dictionary kes),
# fstrings will not play so well. You have to either escape matching quotes, or use different
# quote marks for the main string and sub-strings. I recomend using different quotes as it's more readable than \" \"

#calculation = "4 times 11 is equal to {}".format(4*11)
calculation = f"4 times 11 is equal to {4*11}"
print(calculation) #returns 44
#Since fstrings are evaluated like any other expression, you can perform
# logical and mathmatical operations within them

for i in range(1, 11):
    sentence = f"the current value is {i:03}"
    print(sentence)
#You can also apply additional formatting, in the same way you apply any other string formatting.

#further demonstration that fstrings allow for additional formatting
pi = 3.141592
sentence = f"The value of Pi is aproximately {pi:.4f}" #only prent to four digits.
print(sentence)

print("importing datetime...")
from datetime import datetime
print("done!")
birthday = datetime(1990, 1, 1) #the birthday of computer time!
sentence = f"The aniversary of computer time is {birthday:%B %d, %Y}"
print(sentence)
#As this shows, this works with formats even from other modules.

