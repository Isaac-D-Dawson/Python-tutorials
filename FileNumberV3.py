#Filenumering V3

import os

os.chdir(r'FileManipulation\FileNumberV3 07.01.2020')
origFiles = [f for f in os.listdir()]
trackIndex = [f"#{i}_" for i in range(1, 11)] #patch to use "1, filecount+1"
#tracksZipped = zip(origFiles, trackIndex)
#print(origFiles)

sortedFiles = []
#sortedFiles = [f"{i.split("_")[-1]}@{i}" for i in origFiles]
for i in origFiles:
    file_name = i.split("_")[-1]
    sortedFiles.append(f"{file_name}@{i}")

print(sortedFiles)
tracksZipped = zip(sorted(sortedFiles), trackIndex)

for f in tracksZipped:
    tracks = f[0].split("@")
    #print(tracks[1], f"{f[1]}{tracks[0]}")
    os.rename(tracks[1], f"{f[1]}{tracks[0]}")