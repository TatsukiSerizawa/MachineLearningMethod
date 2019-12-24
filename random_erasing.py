# Random Erasing of Image Data Augumentation

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from keras.datasets import cifar10


(train_X, train_y), (test_X, test_y) = cifar10.load_data()

train_X = train_X.astype('float32') / 255
test_X = test_X.astype('float32') / 255

# show images
def show_images(dataset):
    for i in range(4):
        fig = dataset[i]
        plt.imshow(fig)
        plt.show()

# Random Erasing
def random_erasing(img):
    p = 0.5
    s_l, s_h = 0.02, 0.4
    r1, r2 = 0.3, 1.0 / 0.3
    
    p1 = np.random.uniform(0, 1)

    if p1 < p:
        return img
    else:
        H, W = img.shape[0], img.shape[1]
        S = H * W
        while True:
            S_e = S * np.random.uniform(low=s_l, high=s_h)
            r_e = np.random.uniform(low=r1, high=r2)

            H_e = np.sqrt(S_e * r_e)
            W_e = np.sqrt(S_e * r_e)

            x_e = np.random.randint(0, W)
            y_e = np.random.randint(0, H)

            if x_e + W_e <= W and y_e + H_e <= H:
                img_erased = np.copy(img)
                img_erased[y_e:int(y_e + H_e), x_e:int(x_e + W_e), :] = np.random.uniform(0, 1)
                return img_erased

train_X_erased = np.copy(train_X)
for i in range(train_X_erased.shape[0]):
    train_X_erased[i] = random_erasing(train_X_erased[i])

show_images(train_X_erased)