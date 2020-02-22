import numpy as np 
import matplotlib.pyplot as plt
import os


def plot_images(imgs, lbls=None, cols=4, rows=5, save_path=None):
    """
    A function which plots multiple images
    param:
        imgs    -   list of images 
        lbls    -   if given, list of labels for the images
        cols    -   number of columns
        rows    -   number of rows
    """
    # numpy array to list
    if not type(imgs) is list:
        imgs = list(imgs)
    # 1. check if the parameters are correct
    assert(len(imgs) == cols*rows)
    if not lbls is None:
        assert(len(lbls) == len(imgs))

    # 2. create the figure
    fig = plt.figure()

    # 3. iterate over the rows and cols
    for i in range(1, cols*rows + 1):
        # add the next subplot
        fig.add_subplot(rows, cols, i)
        # plot the image
        plt.imshow(imgs[i-1])
        # check if a lbls list is specified
        if not lbls is None:
            # show the lbl of the image
            plt.title(lbls[i-1])
    plt.tight_layout(pad=0.6)

    if not save_path is None:
        plt.savefig(save_path)
    else:  
        plt.show()