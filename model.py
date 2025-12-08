import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix


df = pd.read_csv('data/data_cleaned.csv', na_values=['NA'])
numeric_df = df.select_dtypes(include=['number'])
correlations = numeric_df.corr()['treatment'].sort_values(ascending=False)
print(correlations)


# Keep top correlated features
X = df[[
    'family_history',
    'work_interfere',
    'care_options',
    'obs_consequence',
    'leave']]
y = df['treatment']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
