from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
import pandas as pd


# 1. Prepare features and target

data_df = pd.read_csv("../data/processed/winequality-red-wrangled.csv", sep=',')

X = data_df.drop(columns=["quality", "label"])
y = data_df["label"]

# 2. Split data (Stratified ensures Good/Bad ratio remains the same)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=123, stratify=y
)

# 3. Train Logistic Regression
lr_model = LogisticRegression(max_iter=2000)
lr_model.fit(X_train, y_train)

# 4. Show Classification Report
y_pred = lr_model.predict(X_test)
print(classification_report(y_test, y_pred))

# 5. Plot Confusion Matrix
disp = ConfusionMatrixDisplay.from_estimator(lr_model, X_test, y_test, cmap=plt.cm.Blues)
plt.title("Confusion Matrix: Logistic Regression")
plt.savefig("../results/confusion_matrix.png", dpi=300)
