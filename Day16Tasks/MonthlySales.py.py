import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)
plt.plot(df["Month"], df["Sales"], marker="o")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.grid()

plt.show()