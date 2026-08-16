import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])

departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Department": departments, "Salary": salaries})

department_salary = df.groupby("Department")["Salary"].mean()

department_counts = df["Department"].value_counts()

figure, axes = plt.subplots(2, 3, figsize=(15, 8))

axes = axes.flatten()

axes[0].plot(df.index, df["Salary"], marker="o")

axes[0].set_title("Salary Trend")

axes[0].set_xlabel("Employee Index")

axes[0].set_ylabel("Salary")

axes[1].bar(department_salary.index, department_salary.values)

axes[1].set_title("Average Salary by Department")

axes[1].set_xlabel("Department")

axes[1].set_ylabel("Average Salary")

axes[2].pie(department_counts.values, labels=department_counts.index, autopct="%1.1f%%")

axes[2].set_title("Department Distribution")

axes[3].hist(df["Salary"], bins=5, edgecolor="black")

axes[3].set_title("Salary Distribution")

axes[3].set_xlabel("Salary")

axes[3].set_ylabel("Frequency")

axes[4].scatter(df.index, df["Salary"])

axes[4].set_title("Index vs Salary")

axes[4].set_xlabel("Employee Index")

axes[4].set_ylabel("Salary")

figure.delaxes(axes[5])

plt.tight_layout()

plt.show()