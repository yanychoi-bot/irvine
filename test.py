import pandas as pd

# Load your CSV file
df = pd.read_csv('jobs.csv')

# Remove rows where the Salary column is empty
df = df[df['Salary'].notna()]

# Save the modified DataFrame back to a CSV file
df.to_csv('newjobs.csv', index=False)
