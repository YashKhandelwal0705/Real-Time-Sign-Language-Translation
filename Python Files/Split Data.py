import os
import random
import shutil
from itertools import islice

outputFolderPath = "D:/Projects/SLT/New Dataset/SplitData"
inputFolderPath = "D:/Projects/SLT/New Dataset/L - Right"
splitRatio = {"train":0.7, "val":0.2, "test":0.1}



#Directories to create

#Training
os.makedirs(f"{outputFolderPath}/train/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels", exist_ok=True)

#Validation
os.makedirs(f"{outputFolderPath}/val/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels", exist_ok=True)

#Testing
os.makedirs(f"{outputFolderPath}/test/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels", exist_ok=True)

#Get the names
listNames = os.listdir(inputFolderPath)
print(len(listNames))
uniqueNames=[]
for name in listNames:
    uniqueNames.append(name.split('.')[0])
uniqueNames=list(set(uniqueNames))

print(len(uniqueNames))



#Shuffle
random.shuffle(uniqueNames)


#Find the number of images for each folder
lenData = len(uniqueNames)
lenTrain = int(lenData*splitRatio['train'])
lenVal = int(lenData*splitRatio['val'])
lenTest = int(lenData*splitRatio['test'])

#Put remaining images in training
if lenData!=lenTrain+lenTest+lenVal:
    remaining =lenData-(lenTrain+lenTest+lenVal)
    lenTrain+=remaining
print(f"Total Images: {lenData}\nSplit: {lenTrain} {lenVal} {lenTest}")

#Split the list
lenToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lenToSplit]
print(f"Total Labels: {lenData}\nSplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}")

#Copy the files

sequence = ['train', 'val', 'test']
img_exts = ('.jpg','.jpeg','.png')
for i, out in enumerate(Output):
    for filename in out:
        for extn in img_exts:
            image_path = f"{inputFolderPath}/{filename}{extn}"
            label_path = f"{inputFolderPath}/{filename}.txt"

            # Check if both image and label exist
            if os.path.exists(image_path) and os.path.exists(label_path):
                shutil.copy(image_path, f"{outputFolderPath}/{sequence[i]}/images/{filename}.jpg")
                shutil.copy(label_path, f"{outputFolderPath}/{sequence[i]}/labels/{filename}.txt")
print("Split process completed")
