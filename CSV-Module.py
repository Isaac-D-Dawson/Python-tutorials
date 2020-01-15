#comma seperated values handling module.py      13.11.2019

import csv

# with open("names_redo.csv", "r") as oldCsvFile:
#     csv_reader_orig = csv.reader(oldCsvFile)
#     #next(csv_reader)
#     with open("new_names_redo.csv", "w") as newCsvFile:

#         for items in csv_reader_orig:
#             #print(items)
#             for index, content in enumerate(items):
#                 newCsvFile.write(content)
#                 #print(index)
#                 #print(content)
#                 if index != 2:
#                     newCsvFile.write("+")
#             newCsvFile.write("\n")

# with open("names_redo.csv", "r") as oldCsvFile:
#      with open("new_names_redo.csv", "w") as newCsvFile:
#         csv_read = csv.reader(oldCsvFile)
#         csv_write = csv.writer(newCsvFile, delimiter="\t")

#         for line in csv_read:
#             csv_write.writerow(line)
#             print(line)

with open("names_redo.csv", "r") as input:
    with open("new_names_redo.csv", "w") as output:
        csv_reader = csv.DictReader(input)

        for i in csv_reader:
            print(i)