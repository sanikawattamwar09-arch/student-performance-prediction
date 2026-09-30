import pandas as pd
import joblib

data = pd.read_csv("data/student_performance.csv")

print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

# Features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments_completed"
    ]
]

# Target
y = data["result"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print(X_train.shape)

print("\nTesting data:")
print(X_test.shape)









print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)


from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Make predictions on test data
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)



from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Predict for a new student

new_student = [[7, 85, 75, 9]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nNew Student Prediction: Pass")
else:
    print("\nNew Student Prediction: Fail")



# Save the trained model
joblib.dump(model, "model/student_model.pkl")

print("\nModel saved successfully!")