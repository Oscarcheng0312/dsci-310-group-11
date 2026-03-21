import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure a directory exists for our figures
Path("../results").mkdir(parents=True, exist_ok=True)

data_df = pd.read_csv("../data/processed/winequality-red-wrangled.csv", sep=',')


plt.figure(figsize=(8, 5))
# Use box plots to compare the alcohol content distribution of good and bad wines.
sns.boxplot(x='label', y='alcohol', data= data_df, palette='Set2', hue = 'label', legend = False)

plt.xlabel("Wine Quality Category", fontsize=12)
plt.ylabel("Alcohol Content (% vol)", fontsize=12)
plt.title("Alcohol Content by Wine Quality Label", fontsize=14)
plt.tight_layout()
plt.savefig('../results/eda_boxplot.png')
