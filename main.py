import sys
import plt_graphs_and_charts


QUESTION = "What would you like to do? Only enter the numeric value"
OPTIONS = {
    "1: draw a line": plt_graphs_and_charts.draw_a_line,
    "2: draw two points": plt_graphs_and_charts.draw_two_points,
    "3: draw a line with more points": plt_graphs_and_charts.draw_a_line_with_more_points,
    "4: draw 2 plots with title and super title": plt_graphs_and_charts.draw_2_plots_with_title_and_super_title,
    "5: draw 6 plots": plt_graphs_and_charts.draw_6_plots,
    "6: load the csv data": plt_graphs_and_charts.read_csv,
    "7: draw a scatterplot": plt_graphs_and_charts.create_scatter_plot,
    "8: draw a barchart using the LinkedIn search_data": plt_graphs_and_charts.create_barchart_with_linkedin_data,
    "9: exit the program": sys.exit
}


def main():
    while True:
        print(QUESTION)
        for option in OPTIONS.keys():
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
