# **Data Analysis Report** - Yonghwan Choi

1. **What is the purpose of the analysis?**
   > Define the goal or objective of your analysis. Are you exploring patterns, relationships, outliers, or trying to gain insights into a specific aspect of the data?

- This analysis intends to find the relation between the wage of a job and the location of the workplace.
- The analysis includes remote jobs, which are known to have the least bonds to physical offices comparing to other jobs.

2. **What is the structure of the dataset?**
   > Understand the size of the dataset, the number of variables, and the types of variables (categorical, numerical, etc.).

- There are 4 columns (Title,Company,Location,Salary).
  - Title : string variable which is the job title itself.
  - Company : string variable which is the company that opened this job.
  - Location : string variable indicating the location of the job.
  - Salary : float variable indicating the hourly wage of the job.
- The dataset includes 1,278 rows of data, presenting all columns. Location and company data can be used for categorizing salary values (e.g. hourly wage by company, location, etc.)

3. **What are the key features or variables in the dataset?**
   > Identify the main variables that are relevant to your analysis.

- The most valuable and important variable of all is the salary data. This is the actual key value I want to predict, and the most precise and objective value to weigh a job. Company and Location are the values used for visualization & data clarification.

4. **Are there missing values in the dataset?**
   > Check for missing data and decide on a strategy for handling it (e.g., imputation, removal).

- I have error handling in the crawling code for removing incomplete data within the dataset. It removes the partial data so that data with full information will only be used.

  ```python
  import csv
  print(len(jobs))

  with open('jobs.csv', 'w') as f:
      writer = csv.writer(f)
      writer.writerow(['Title', 'Company', 'Location', 'Salary'])
      for job in jobs:
          try:
              writer.writerow([job.title, job.company, job.location, get_salary(job.salary)])
          except:
              pass
  ```

5. **What are the summary statistics of numerical variables?**
   > Calculate basic statistics such as mean, median, standard deviation, etc., to understand the central tendency and dispersion of numerical variables.

- The statistics for this dataset is as follows:

  - Mean: 27.360367762128327
  - Median: 21.5
  - Standard Deviation: 15.885060048807812
  - Minimum: 15.5
  - Maximum: 250.0

  These values were calculated with this code:

  ```python
  import pandas as pd

  # Load the CSV file
  df = pd.read_csv('jobs.csv')

  # Assuming 'Salary' is a column with numerical values
  # If 'Salary' contains non-numerical values or symbols, they should be cleaned or converted to numerical values first

  # Calculate statistics
  mean_salary = df['Salary'].mean()
  median_salary = df['Salary'].median()
  std_dev_salary = df['Salary'].std()
  min_salary = df['Salary'].min()
  max_salary = df['Salary'].max()

  # Display the results
  print("Salary Statistics:")
  print(f"Mean: {mean_salary}")
  print(f"Median: {median_salary}")
  print(f"Standard Deviation: {std_dev_salary}")
  print(f"Minimum: {min_salary}")
  print(f"Maximum: {max_salary}")

  ```

6. **How are categorical variables distributed?**

   > Examine the distribution of categorical variables through frequency tables or visualizations.

7. **Are there any outliers in the data?**

   > Identify and assess the presence of outliers in numerical variables.

8. **What is the distribution of the target variable (if applicable)?**

   > If you have a target variable (e.g., in a predictive modeling scenario), understand its distribution.

9. **Are there any patterns or trends over time?**

   > If time is a factor, explore whether there are any temporal patterns or trends.

10. **Are there correlations between variables?**

    > Use correlation matrices or scatter plots to investigate relationships between numerical variables.

11. **How does the data vary across different groups or categories?**

    > Compare subsets of the data to understand variations across different groups or categories.

12. **What visualizations can help in understanding the data better?**

    > Consider using visualizations like histograms, box plots, scatter plots, etc., to gain insights.

13. **What preprocessing steps might be necessary for further analysis?**

    > Identify any preprocessing steps needed, such as scaling, encoding categorical variables, or handling outliers.

14. **Are there any unusual patterns or unexpected findings?**

    > Look for patterns that are unexpected or may require further investigation.

15. **What are the limitations of the dataset?**
    > Recognize any limitations or potential biases in the data that may impact your analysis.
