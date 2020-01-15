with open("names_redo.csv", "r+") as target:
    data_in = target.readlines()
    target.seek(0)
    data_out = [i for i in data_in if i != ",,\n"]
    print(data_out)
    for i in data_out:
        target.write(i)
        print(i)