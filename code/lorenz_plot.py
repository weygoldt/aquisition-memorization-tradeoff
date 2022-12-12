import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

testdf = pd.DataFrame({'levels1': [0,0,1,1], 'levels2': [2,8,2,8], 'data': [0.1, 0.2, 0.3, 0.4]})
sns.catplot(x='levels2', y='data', hue='levels1', data=testdf, kind='bar')
plt.show()
