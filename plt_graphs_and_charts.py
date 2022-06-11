import matplotlib.pyplot as plt
import numpy as np
import sys


def draw_a_line():
    """Draw a line in a diagram from position (0,0) to position (6,250)"""
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()


def draw_two_points():
    """Draw two points in the diagram, one at position (1, 3) and one in position (8, 10)"""
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints, 'o')
    plt.show()


def draw_a_line_with_more_points():
    """Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)"""
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


QUESTION = "What would you like to do? Only enter the numeric value"
OPTIONS = {
    "1: draw a line": draw_a_line,
    "2: draw two points": draw_two_points,
    "3: draw a line with more points": draw_a_line_with_more_points,
    "4: draw 2 plots with title and super title": draw_2_plots_with_title_and_super_title,
    "5: draw 6 plots": draw_6_plots,
    "6: exit the program": sys.exit
}


def main():
    while True:
        print(QUESTION)
        for option in OPTIONS.keys():
            # print(f"{option}.__qualname__")
            print(f"{option}")
        user_choice_index = input()
        for choice in OPTIONS:
            if user_choice_index + ":" in choice:
                match = choice
                break

        function = OPTIONS[match]
        function()  # execute the code for the user's choice
        # ask again


if __name__ == "__main__":
    main()
