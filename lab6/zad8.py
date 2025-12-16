import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "czas": [0, 1, 2, 3, 4, 5],
    "predkosc": [0, 10, 25, 40, 45, 50]
})


plt.scatter(df["czas"], df["predkosc"])
plt.xlabel("Czas [s]")
plt.ylabel("Prędkość [m/s]")
plt.title("Prędkość chwilowa pojazdu")
plt.grid(True)
plt.show()
