import os
input_dir = r"D:\Projects\SLT\New Dataset\Y - Copy"
files = [f for f in os.listdir(input_dir) if f.lower().endswith('.txt')]
del_cnt = 0
for f in files:
    lab_path = os.path.join(input_dir,f)
    with open(lab_path,'r') as file:
        lines = file.readlines()
    remove = False

    for line in lines:
        parts = line.strip().split()
        if len(parts)>5:
            remove = True
            break
        _,x,y,h,w = map(float,parts)
        if any(val<0 or val>1 for val in [x,y,h,w]):
            remove = True
            break
    if remove:
        os.remove(lab_path)
        image_path = os.path.join(input_dir, os.path.splitext(f)[0] + ".jpg")
        if os.path.exists(image_path):
            os.remove(image_path)
        del_cnt += 1
        print(f"Deleted image and label file {f}")
print(f"Total deleted images: {del_cnt}")


