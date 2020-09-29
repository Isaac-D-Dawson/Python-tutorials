#re-module.py       17.02.2020

#import the regex module, and let the user know it's installed.
import re
print("regex module installed")

#A rawstring in python is a string prefixed with "r", which tells python to ignore escape characters
print(r"\n test")
#versus
print("\n test")

#re.compile() method



text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r"abc")

#find the matches
# matches equals the pattern, which we find in(text_to_search)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    #returns an object that contains both the search key, and the indexes(last digit exclusive).
    #just to test
# print(text_to_search[1:4])
# #returns our searched key.

#lets jsut put in a newline to make thins easier to read:
print("\n")

#lets do this again, searching for all "." charachters.
pattern = re.compile(r"\.") #  just a "." would match all charachters, not just ".", so we need to escape it.

#find the matches
# matches equals the pattern, which we find in(text_to_search)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    #remember: if you need to find a "." in something, be sure to escape it!

#list of metachachters:
# ".":  matches every non-newline char
# "\d": matches every digit from 0-9
# "\D": matches everything that is NOT a digit
# "\w": matches all letters- regardless of case, all digits, and "_" chars.
# "\W": matches anything that \w doesnt.
# "\s": matches any whitespace chars(" ",  "    ", and "
# "\s or spaces, tabs and newlines)
# "\S": any NON-whitespace chars, the oposite of \s
# These next ones are called "Anchors" and don;t seach for the chars themselves, but
# more change where and how things are searched.
# "\b": Word Boundary. Chars that are whitespace or Not alpha numeric.
# "\B": not word boundary, chars that are alphanumeric?
# "^": start of string.
# "$": end of string
# "[]": matches any of the chars inside the brackets
# "[^]": matches anything but the chars in the brackets.

#Note that capitalised versions of letters tend to match the oposite of the lowercase versions.

#print a newline for neatness
print("\n")

pattern = re.compile(r"\bHa") 

#find the matches
# matches equals the pattern, which we find in(text_to_search)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    #returns the first and the second "Ha"",but not the last. The first one is preceded by a \n, and 
    # the second by a space, which both trigger the word border. The thrid however is preceded by 
    # an a, which does not trigger the word boundary.

print("\n")

pattern = re.compile(r"^Start") # This will find whatever we pass in, as long as it's at the start of the string.

#find the matches
# matches equals the pattern, which we find in(sentance)
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

print("\n")

pattern = re.compile(r"start$") #matches whatever is passed in as long as it's at the End of the string

#find the matches
# matches equals the pattern, which we find in(sentence)
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
    
#back to "text_to_search"

print("\n")

pattern = re.compile(r"\d*[-\.]\d*[-\.]\d*") 

#find the matches
# matches equals the pattern, which we find in(text_to_search)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

with open("RE.data.txt", "r") as data:
    contents = data.read()
    pattern = re.compile(r"\w*@bogusemail\.com")
    matches = pattern.finditer(contents)
    for index, i in enumerate(matches, start=1):
        print(index, i)
print("\n")

pattern = re.compile(r"\d{3}[-\.]\d{3}[-\.]\d{4}") 

#find the matches
# matches equals the pattern, which we find in(text_to_search)
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print("\n")
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r".*@.*\.(com|edu|net)")
matches = pattern.finditer(emails)
for i in matches:
    print(i)

print("\n")
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#Each group gets an identifier, starting a 1. group 0 is all collected input.
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
subbedUrls = pattern.sub(r"\2\3", urls)#backreference. lets you edit groups:
# you can swap groups, or replace the contents of a given group entirely. 
print(subbedUrls) #using "".group(num)" returns the group of the given number
#if there is no data in a group, it will return none.

#Continued on 18/02.2020

print("\n")
#Here we'll use findall() instead of finditer()
pattern = re.compile(r".+")
matches = pattern.findall(urls)
for i in matches:
    print(i)
    #the output here returns each searched fro group as a touple.
    # It will only return the groups you requested and not group 0.
    # Note that it will return everything that matches you searched for, and not
    # the location of it like finditer() does. This is useful, in different ways.
    # Keep this in mind, and test your code as much as possible.

print("\n")
#Testing the match() method
pattern = re.compile(r"Start")
matches = pattern.match(sentence)
print(matches)
#"match()"" returns the same "r.match..." object, however it will only
# return the first match it finds, and nothing else.
# It will also only search at the begining of targets...I..I have no idea.

sentence = 'start a sentence and then bring it to an end. This does not start here.'

print("\n")
#Testing the search() method
pattern = re.compile(r"start", re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)
# "search()" behaves similarly to match, however it searches the entire string for the target data.
# This could be used as a check to see of any target data is present, but
# in general for proper searching, use finditer(). it is the more useful of the two.
# if no match is found, it will return "None".

# print("\n")
# #Using flags
# #Flags can be parsed into the re.compile() method to affect how the search is handled.
# pattern = re.compile(r"start", re.IGNORECASE)
# matches = pattern.finditer(sentence)
# for i in matches:
#     print(i)
# #Here as you can see, the match returned "Start", even though we searched for "start".
# # Flags can be used to cover for unknowns in collected data, and to simplify
# # overcomlicated RegEx patterns.
