import pandas as pd
from pathlib import Path

raw_data_dir = Path("../data/raw")
raw_data_dir.mkdir(parents=True, exist_ok=True) 

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
file_path = raw_data_dir / "winequality-red.csv"

print(f"Downloading data from {url}...")

df = pd.read_csv(url, sep=';')
print(f"The correct dimensions for red wine data should be: {df.shape}")

df.to_csv(file_path, index=False)
print(f"The data has been successfully downloaded and saved to: {file_path.resolve()}")