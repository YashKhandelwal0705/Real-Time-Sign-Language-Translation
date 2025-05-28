import os
outputFolderPath = "D:/Projects/SLT/New Dataset/SplitData"

#Creating data.yaml file
classes = ['A', 'F', 'L', 'Y']
dataYaml = f'path: D:/Projects/SLT/New Dataset/SplitData\n\
train: train/images\n\
val: val/images\n\
test: test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'


f = open(f"{outputFolderPath}/data.yaml", "a")
f.write(dataYaml)
f.close()

print("Data.yml file created.....")