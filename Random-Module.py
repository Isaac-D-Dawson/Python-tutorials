#Random Module      08.01.2020

#Importing the random module for use in this document:
import random as rand
#included in standard libary, no additional install needed.

#Print all the functions from rand
# for i in dir(rand):
    # print(i)

#Note that all values are floats(to 16 Significa figures?) unless
# otherwise specified.

print(rand.random())
#Returns a random value between 0 and 1, inc, exc
print(rand.uniform(1, 10))
#Returns a random value in the range specified, inc, exc
print(rand.randint(1, 10))
#Returns a random int between the two arguments, inc, inc
#Raxample code for tossing a coin:
# coin = ["heads", "tails"]
# print(coin[rand.randint(0, 1)])
#Better alternative
print(rand.choice(["heads", "tails"]))
#The ".choice()" method take in a list, and returns a random item from that list.
# Note this also works with tuples.


print(rand.choices(["Heads", "Tails", "Edge"], weights=[4, 4, 1], k=10))
#the "".choices()" method behaves like the ".choice()" method, but runs multiple
# times to return a list of options. It takes in several keywords:
#  The key "k" is required, and determines how many times to run.
#  The key "weights" determines how likely it should pick any given
# option from the list. the weights are paired to the input list's index.

deck = list(range(1, 53))
print(deck)
rand.shuffle(deck)
print(deck)
#".shuffle()" re-orders a provided list randomly.
# keep in mind it will not check if the list matches the original, and
# that it pverwrites the original.

#Weird borkeny thing
# coin = {"0":"heads", "1":"tails"}
# print(rand.choice(coin))

