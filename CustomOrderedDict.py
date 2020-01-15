

with open("small_names_redo.csv", "r") as input:
    def oDict(rFile):
        #keys = rFile.readline()     
        keys = (rFile.readline().strip("\n").split(","))
        #Get keys from first line
        dicts = []                  #Generate an empty dictionary to store the dicts in

        print(keys)

        for i in rFile.readlines():
            dicts.append({keys[0]:i.strip("\n").split(",")[0], keys[1]:i.strip("\n").split(",")[1], keys[2]:i.strip("\n").split(",")[2]})
        print(dicts)
        print(dicts[0])

    oDict(input)

