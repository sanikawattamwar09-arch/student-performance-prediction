import joblib

# Load the trained model
model = joblib.load("model/student_model.pkl")

# Enter student details
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous score: "))
assignments_completed = int(input("Enter assignments completed: "))

# Make prediction
new_student = [[
    study_hours,
    attendance,
    previous_score,
    assignments_completed
]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nPrediction: Pass")
else:
    print("\nPrediction: Fail")