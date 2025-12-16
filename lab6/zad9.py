import matplotlib.pyplot as plt

oceny = [4.5, 3.0, 5.0, 4.0, 2.5]

plt.hist(oceny, bins=5, edgecolor="black")
plt.title("Rozkład ocen studentów")
plt.xlabel("Ocena")
plt.ylabel("Liczba studentów")
plt.show()
