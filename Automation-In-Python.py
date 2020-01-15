#automation in python       07.01.2019

import os

os.chdir(r'FileManipulation\FileNumberV2 07.01.2020')
origFiles = [f for f in os.listdir()]
#origFiles = [i for i in os.listdir('FileManipulation')]
#This works, but keep ind mind it might be harder to read.

#os.path.splitext(f) use to split extensions form files, retuirns a tuple

#V2 additions are tagged "V2:"

#V2: split off all the original numbering
trackNames = [i.split("_")[-1] for i in origFiles]

trackIndex = [f"#{i}_" for i in range(1, 11)]
tracksZipped = zip(trackNames, trackIndex)
#V2: updated zip with new list of stripped names
tracksZipped = zip(origFiles, tracksZipped)

#print(origFiles)
#print(trackIndex)

for i in tracksZipped:
    os.rename(i[0], f"{i[1][1]}{i[1][0]}")
    #print(i[0], f"{i[1][1]}{i[1][0]}")
    pass