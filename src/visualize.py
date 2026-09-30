import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/student_performance.csv")

# Create scatter plot
plt.scatter(
    data["study_hours"],
    data["previous_score"],
    c=data["result"]
)

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")

plt.show()