from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

### 引数としてimage_nameう受け取り
### numpy配列化してsave_data.npyをreturnする
classes = ["image1", "image2", "image3"]
num_classes = len(classes)
# rezie image data to 50 pixels
image_size = 50

# input image data
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
np.save("./save_gendata.npy", xy)

