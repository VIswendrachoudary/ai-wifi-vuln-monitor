from sklearn.ensemble import RandomForestClassifier
import joblib

# Fake training data: 0 = weak, 1 = strong encryption
X = [[0], [1]]
y = [0, 1]

clf = RandomForestClassifier()
clf.fit(X, y)

# Save the model
joblib.dump(clf, "wifi_model.pkl")
print("Model trained and saved as wifi_model.pkl")
