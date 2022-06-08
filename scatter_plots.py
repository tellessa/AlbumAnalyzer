import matplotlib.pyplot as plt
import numpy as np


def create_scatter_plot():
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    create_scatter_plot()
