from bank import database,time_convert
import time

##################################################################
#                         Your Mission                           #
##################################################################

# 1) identify the number of accounts in the database
# 2) access each account and withdraw £5............
# 3) update the database with new value after you have within drawn your desired amount....
# 4) add the withdrawn amount to the spoofed_account

#thing to keep in mind
#you will need to assign the imported database to data_
#gather some intel from Bank on how to do this....

data_ = database()
spoofed_account = [] #this means an empty list 

# to figure out the number of accounts in the bank you may want to loop over the database
# using a 'for loop'

# #for loop use case example:
# greetings = ['hello','goodday','howdy','yo','sup']

# for greeting in greetings: # take note of the ':'
#     print(greeting) # and also the indentation!!

# # the for loop is a very powerful tool that may save you time....
# # other tools you may need:
# #type() 
# #str()
# #int()

# # .append() use case example:
# print(f'Account Before :{spoofed_account}')
# spoofed_account.append(f'£{100}')
# print(f'Account After :{spoofed_account}')

# # # .strip('?') use case example:
# # var = 'A string'
# # print(f'Before: {var}')
# # var = var.strip('A') #remember strings are immutable 
# # print(f'After: {var}')





########################################################
#                 END OF INSTRUCTIONS                  #
########################################################

#what the accounts look like before your hack
print(f'Before: {data_}')

########################################################
#your code goes below !!
t0 = time.time()
########################################################

#data_ = database()
spoofed_account = ["Avery T D Harry", "£0"]

#print(help(int()))
targets = data_.index(data_[-1])
print(f"number of accounts targeted:{targets+1}")

for i in data_:
    money = i[1].strip("£")
    i[1] = (f"£{int(money)-5}")
    funds = spoofed_account[1].strip("£")
    spoofed_account[1] = (f"£{int(funds)+5}")
    

#########################################################
t1 = time.time()
#########################################################

#what the accounts look like after your hack
print(f'After: {data_}')

#########################################################

t = t1-t0
print(f'your hack took {time_convert(t)}')

