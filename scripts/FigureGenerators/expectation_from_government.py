import pandas as pd

from Base.FigureController import Controller


class ExpectationFromGovernmentFigureController(Controller):
    figure_width = 6
    directory_name = "Expectation_From_Government.eps"
    question = "What are your expectations from the Government?"


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/government.csv")
    controller = ExpectationFromGovernmentFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)
