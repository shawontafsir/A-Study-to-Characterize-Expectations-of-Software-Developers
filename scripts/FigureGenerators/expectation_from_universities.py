import pandas as pd

from Base.FigureController import Controller


class ExpectationFromUniversityFigureController(Controller):
    directory_name = "Expectation_From_Universities.eps"
    question = "What are your expectations from the universities?"


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/universities.csv")
    controller = ExpectationFromUniversityFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)
