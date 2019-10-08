#Strings

#single quotes
message = 'Hello World'
print(message)

#using double quotes to avoid error from apostrophe.
message = "Bobby's World"           
print(message)

#using an escape(\) to handle apostrophe
message = 'Bobby\'s World'
print(message)

#triplestrings/docstrings(Strings in three sets of quotes) hold true over multiple lines
message = """I'm singing in the rain
just singing in the rain"""
print(message)
#strings NOT in this format will NOT work over multiple lines

#function len() , short for length, returns the length of the string, starting at 1
message = "abcdefg"
print(len(message))

#Strings are just strings of characters, and you can request specific characters using [].
message = "abcdefg"
print(message[0])
#Keep in mind that the first character is stored at 0, second at 1, ETC.

#calling a negative number inside [] prints the digit that number from the end, starting a -1
message = "abcdefg"
print(message[-1])

#Using : indicates a range (This number to This number),
message = "Hello World"
print(message[0:5])
#Note the first index is INCLUSIVE, the output will include this value
#the second is EXCLUSIVE, it will NOT return this value
#EG: The range "0:1" will only return slot 0
#Note that you do not need to include 0 when starting from 0.

#Methods are functions called from objects

#Using .lower() on a string returns that string, all in lowercase
message = "HeLlO wOrLd"
print(message.lower())

#using .upper()returns the string in all UPPERCASE
message = "HeLlO wOrLd"
print(message.upper())

# the .count method takes an input argument, and counts all occurances of that input in a string.
message = "aaabbbb"
print(message.count("b"))
#Note that .count() can be passed entire strings