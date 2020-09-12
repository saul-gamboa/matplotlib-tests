import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 9]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label="Linea 1")
plt.plot(x2, y2, label="Linea 2")
plt.xlabel("Entrada")
plt.ylabel("Resultado")
plt.title("Título \n Subtítulo")
plt.legend()
plt.show()
