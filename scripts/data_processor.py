import pandas as pd
from pathlib import Path


df_wrangled = pd.read_csv('../data/raw/winequality-red.csv')
df_wrangled["label"] = df_wrangled["quality"].apply(lambda x: "Good" if x >= 6 else "Bad")

processed_dir = Path("../data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)
df_wrangled.to_csv(processed_dir / "winequality-red-wrangled.csv", index=False)

print(df_wrangled["label"].value_counts())
df_wrangled.head()