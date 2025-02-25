import matplotlib.pyplot as plt

# Data for CRM Accuracy
labels = ['Accurate Data', 'Incorrect Data']
sizes = [90, 10]  # Example accuracy ratio
colors = ['#28a745', '#dc3545']  # Green for accurate, Red for incorrect
explode = (0.1, 0)  # Explode first slice for emphasis

# Create Pie Chart
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, startangle=90)
plt.title('CRM Data Accuracy')
plt.show()