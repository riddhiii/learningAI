
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya", "Dev"],
    "Hours": [2, 4, 3, 5, 1],
    "Marks": [50, 85, 70, 95, 40]
}

df = pd.DataFrame(data)

plt.scatter(df["Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()


