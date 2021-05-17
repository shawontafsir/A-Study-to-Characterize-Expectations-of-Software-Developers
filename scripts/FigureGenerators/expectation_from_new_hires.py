import pandas as pd

from Base.FigureController import Controller


class ExpectationFromNewHiresFigureController(Controller):
    figure_width = 5
    directory_name = "Expectation_From_New_Hires.eps"
    question = "What are your expectations from the new hires?"


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/new_hires.csv")
    controller = ExpectationFromNewHiresFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)
