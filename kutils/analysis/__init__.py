import math
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from functools import partial


def corr(data, target_column, top_n=20):
    corr_df = data.corr().abs()
    s = corr_df.unstack()
    so = s.sort_values(kind="quicksort", ascending=False).reset_index()
    top_df = so[(so['level_0']!=so['level_1']) & (so['level_1'] == target_column)][:top_n]
    top_df = top_df.rename(columns={'level_0':'feature', 'level_1':'target', 0:'corr'})
    return top_df


class GeneralPlotUtils:
    def __init__(self, figsize=(20,4)):
        self.set_figsize(figsize)

    def set_figsize(self, figsize):
        plt.rcParams['figure.figsize'] = figsize
        self.figsize = figsize
