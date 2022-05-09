import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd

PATH_PICS = r"pics"
file_list = os.listdir(PATH_PICS)

for f in file_list:
    img = os.path.join(PATH_PICS,f)
    print(img)