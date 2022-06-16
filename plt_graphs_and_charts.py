
import matplotlib.pyplot as plt
import numpy as np
import sys

import pandas as pd


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


def create_scatter_plot():
    """Scatter plots are used to observe relationships between variables."""
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    plt.scatter(x, y)
    plt.show()


def create_barchart_with_linkedin_data():
    search_results_by_keyword_dataframe, dataframe_info_for_title = read_csv()
    job_postings_with_that_keyword = search_results_by_keyword_dataframe["results"]
    # data = [23, 85, 72, 43, 52]
    keywords = search_results_by_keyword_dataframe["keyword"]
    # labels = ['A', 'B', 'C', 'D', 'E']
    plt.xticks(range(len(job_postings_with_that_keyword)), keywords)
    plt.xlabel("Keyword")
    plt.ylabel("Number of Searches")
    plt.title(dataframe_info_for_title)
    plt.bar(range(len(job_postings_with_that_keyword)), job_postings_with_that_keyword)
    plt.show()


def read_csv():
    search_results_by_keyword_dataframe = pd.read_csv("linkedin_keywords.csv")
    dataframe_info = "Linkedin job search results by keyword:\n"
    print(dataframe_info, search_results_by_keyword_dataframe.head())
    return search_results_by_keyword_dataframe, dataframe_info


QUESTION = "What would you like to do? Only enter the numeric value"
OPTIONS = {
    "1: draw a line": draw_a_line,
    "2: draw two points": draw_two_points,
    "3: draw a line with more points": draw_a_line_with_more_points,
    "4: draw 2 plots with title and super title": draw_2_plots_with_title_and_super_title,
    "5: draw 6 plots": draw_6_plots,
    "6: load the csv data": read_csv,
    "7: draw a scatterplot": create_scatter_plot,
    "8: draw a barchart using the LinkedIn search_data": create_barchart_with_linkedin_data,
    "9: exit the program": sys.exit
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
