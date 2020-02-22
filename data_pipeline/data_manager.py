import os
import numpy as np 
from tqdm import tqdm
import cv2
import pypokedex as dex
import random
import sys
sys.path.insert(0,'..')
import utils

class data_manager:
    """
    Class to manage the pokemon images and additional data.

    only works with pokemon up to dex number 807 until pypokedex is updated.
    simply remove the if statement in the __init__ function if it gets updated!
    """
    def __init__(self, path=os.path.join("..", "clean_pkm")):
        """
        init loads all pokemon images and data.
        it creates a list with images and a list with data/labels
        """
        if not os.path.isdir(path):
            raise NotADirectoryError
        
        self.images = []
        self.pkm = []

        for f_name in tqdm(os.listdir(path)):
            dex_number = int(f_name.split(".")[0].split("_")[0].split("-")[0])

            # remove this in the case of a pypokedex update
            if dex_number <= 807:
                self.images.append(cv2.cvtColor(cv2.imread(os.path.join(path, f_name)), cv2.COLOR_BGR2RGB))
                self.pkm.append(dex.get(dex=dex_number))




if __name__ == "__main__":
    data = data_manager()

    imgs = data.images[0:20]
    lbls = [p.name for p in data.pkm[0:20]]

    utils.plot_images(imgs, lbls=lbls)
