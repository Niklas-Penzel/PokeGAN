import os
import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def clean_data(in_path=os.path.join("..","dirty_pkm"), out_path=os.path.join("..","clean_pkm"), keep_rgba=False):
    if not os.path.isdir(in_path):
        print("WRONG PATH!")
        return 

    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    files = os.listdir(in_path)

    rescale_shape = (64, 64)

    num_c = 4 if keep_rgba else 3
    back_col = 0 if keep_rgba else 0

    for f_name in tqdm(files):
        img = cv2.imread(os.path.join(in_path, f_name), cv2.IMREAD_UNCHANGED)

        height = img.shape[0]
        width = img.shape[1]

        # convert background from rgba to rgb or set background black for rgba
        tmp = np.full((height, width, num_c), back_col, dtype=np.uint8)

        idx = img[:,:,3] == 255
        for i in range(height):
            for j in range(width):
                if idx[i,j]:
                    tmp[i,j,:] = img[i,j,0:num_c]
        img = tmp

        if width > height:
            tmp = np.full((width, width, num_c), back_col, dtype=np.uint8)

            idx = int(width/2) - int(height/2)
            tmp[idx:idx+height,] = img 

            img = tmp
        elif height > width:
            tmp = np.full((height, height, num_c), back_col, dtype=np.uint8)

            idx = int(height/2) - int(width/2)
            tmp[:,idx:idx+width] = img 

            img = tmp

        size = img.shape[0]

        if size > rescale_shape[0]:
            img = cv2.resize(img, rescale_shape, interpolation = cv2.INTER_LANCZOS4)

        cv2.imwrite(os.path.join(out_path, f_name), img)


if __name__ == "__main__":
    clean_data(keep_rgba=True)