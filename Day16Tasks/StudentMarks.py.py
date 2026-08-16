import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

print(df)

plt.bar(df["Student"], df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()