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

#Strings are jsut strings of characters, and you can request specific characters using [].
message = "abcdefg"
print(message[0])
#Keep in mind that the first character is stored at 0, second at 1, ETC.

#calling a negative number inside [] prints the digit that number from the end, starting a -1
message = "abcdefg"
print(message[-1])

