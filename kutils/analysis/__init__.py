import math
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from functools import partial


class GeneralPlotUtils:
    def __init__(self, figsize=(20,4)):
        self.set_figsize(figsize)

    def set_figsize(self, figsize):
        plt.rcParams['figure.figsize'] = figsize
        self.figsize = figsize
