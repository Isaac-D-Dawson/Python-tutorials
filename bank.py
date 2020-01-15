import random as ran
ran.seed(30)

names = ['Mathew','Mark','Luke','Johnny','bruce','Peter','Westley','Ash','Sophie','Louise','Lusy']


security = [f'£{ran.randrange(2000,80000)}' for i in range(0,10)]

#this is a python function but it's not active yet
def database():
    databse = [[i,j] for i, j in zip(names,security)]
    return databse

#this is an instance of the python fucntion above, this instance is active
database()

#print()


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return f'hours:{hours} minutes:{mins} Seconds:{sec}'