import cmocean
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# a colormap can be accessed like thus
colors = cmocean.cm.haline

# but this is only good for plotting continuous things, like heatmaps
# we need categories of colors! We need to discretize it!

# step 1: Cut off maxima and minima of colormap (because too bright or too dark)
new_colors = cmocean.tools.crop_by_percent(cmocean.cm.haline, 40, which='both')

# step 2: Make N discrete colors
N = 6 # eg 6 different colors, must of course be at least as long as the number of objects you want to use this color with
new_discrete_colors = new_colors(np.linspace(0,1,N)) # make them discrete

# now we can test it
mockdata = pd.DataFrame({'data': [1,2,3,4,5,6],
'cat': ['one', 'two', 'three', 'four', 'five', 'six']})
sns.barplot(data=mockdata, x='cat', y='data', palette=new_discrete_colors)
plt.show()