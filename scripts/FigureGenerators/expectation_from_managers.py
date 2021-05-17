import pandas as pd

from Base.FigureController import Controller


class ExpectationFromManagersFigureController(Controller):
    figure_width = 6
    directory_name = "Expectation_From_Managers.eps"
    question = "What are your expectations from your manager?"


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/managers.csv")
    controller = ExpectationFromManagersFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)
