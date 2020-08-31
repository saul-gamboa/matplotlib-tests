import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 9]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label="Firt line")
plt.plot(x2, y2, label="Second line")
plt.xlabel("x-axis")
plt.ylabel("important var")
plt.title("Nice title \n Salu2 Cordiales")
plt.legend()
plt.show()
