import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import rcParams

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('data.csv', sep=',')
print(df.describe())

fig = plt.figure(figsize=(12, 6))
sqft = fig.add_subplot(121)
cost = fig.add_subplot(122)

sqft.hist(df.Windows, bins=80)
sqft.set_xlabel('Rate')
sqft.set_title("Histogram of Windows distribution")

cost.hist(df.Linux, bins=80)
cost.set_xlabel('Rate')
cost.set_title("Histogram of Linux distribution")

plt.show()
