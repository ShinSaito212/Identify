# identify/gen_data_augmented.py

from PIL import Image
import os, sys, glob
import numpy as np
from sklearn import model_selection

### 
# change directory to images
os.chdir("images/")
# get path of images directories
path = os.getcwd()
# list of sub directories
classes = []

for d in os.listdir(path):
    if os.path.isdir(os.path.join(path, d)):
        classes.append(d)

num_classes = len(classes)
# rezie image data to 50 pixels
image_size = 50

# input image data
# X : numpy array, Y : class label
X = []
Y = []

for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")

    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))

        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)

os.chdir("../")
os.chdir("gen/")
np.save("./save_gendata.npy", xy)


