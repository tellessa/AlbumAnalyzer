import matplotlib.pyplot as plt
import numpy as np

# Draw a line in a diagram from position (0,0) to position (6,250):


def draw_a_line():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()

# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):


def draw_two_points():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints, 'o')
    plt.show()

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):


def draw_a_line_with_more_points():
    xpoints = np.array([1, 2, 6, 8])
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(xpoints, ypoints)
    plt.show()


def draw_line_using_default_x_points():
    ypoints = np.array([3, 8, 1, 10, 5, 7])

    plt.plot(ypoints)
    plt.show()


def draw_6_plots():
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(2, 3, 1)
    plt.plot(x, y)

    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(2, 3, 2)
    plt.plot(x, y)

    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(2, 3, 3)
    plt.plot(x, y)

    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(2, 3, 4)
    plt.plot(x, y)

    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(2, 3, 5)
    plt.plot(x, y)

    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(2, 3, 6)
    plt.plot(x, y)

    plt.show()


def draw_2_plots_with_title_and_super_title():
    # plot 1:
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title("SALES")

    # plot 2:
    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(1, 2, 2)
    plt.plot(x, y)
    plt.title("INCOME")

    plt.suptitle("MY SHOP")
    plt.show()


if __name__ == "__main__":
    # draw_a_line_with_more_points()
    # draw_line_using_default_x_points()
    draw_2_plots_with_title_and_super_title()
