import matplotlib.pyplot as plt

# Data
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49']
frequencies = [600, 500, 800, 1000, 600]

# Create bar chart
plt.figure(figsize=(8, 6))
plt.bar(age_groups, frequencies, color='skyblue')

# Add labels and title
plt.xlabel('Age Groups')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a Population')

# Display the plot
plt.show()
