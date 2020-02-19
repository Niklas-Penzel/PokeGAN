import os
import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def clean_data(in_path="dirty_pkm", out_path="clean_pkm"):
    if not os.path.isdir(in_path):
        print("WRONG PATH!")
        return 

    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    files = os.listdir(in_path)

    rescale_shape = (64, 64)

    for f_name in tqdm(files):
        img = cv2.imread(os.path.join(in_path, f_name), cv2.IMREAD_UNCHANGED)

        height = img.shape[0]
        width = img.shape[1]

        # convert fro sRGB to RGB
        tmp = np.full((height, width, 3), 255, dtype=np.uint8)

        idx = img[:,:,3] == 255
        for i in range(height):
            for j in range(width):
                if idx[i,j]:
                    tmp[i,j,:] = img[i,j,0:3]
        img = tmp

        if width > height:
            tmp = np.full((width, width, 3), 255, dtype=np.uint8)

            idx = int(width/2) - int(height/2)
            tmp[idx:idx+height,] = img 

            img = tmp
        elif height > width:
            tmp = np.full((height, height, 3), 255, dtype=np.uint8)

            idx = int(height/2) - int(width/2)
            tmp[:,idx:idx+width] = img 

            img = tmp

        size = img.shape[0]

        if size > rescale_shape[0]:
            img = cv2.resize(img, rescale_shape, interpolation = cv2.INTER_LANCZOS4)

        cv2.imwrite(os.path.join(out_path, f_name), img)


if __name__ == "__main__":
    clean_data()