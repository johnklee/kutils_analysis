import math
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from kutils.analysis import GeneralPlotUtils
from functools import partial


class Utils(GeneralPlotUtils):
    def __init__(self, data, figsize=(20,4)):
        super(Utils, self).__init__(figsize)
        self.data = data


    def treelike_fi(self, model, top_n=20, figsize=None, ytick_fontsize=None, xtick_fontsize=None):
        if figsize is not None:
            self.set_figsize(figsize)
            
        feat_importances = pd.Series(model.feature_importances_, index=self.data.columns)        
        ax = feat_importances.nlargest(top_n).plot(kind='barh')
        if ytick_fontsize:
            ax.set_yticklabels(ax.get_yticklabels(), fontsize=ytick_fontsize)

        if xtick_fontsize:
            ax.set_xticklabels(ax.get_xticklabels(), fontsize=xtick_fontsize)

        return ax
