import pandas as pd

from Base.FigureController import Controller


class ExpectationFromOrganizationFigureController(Controller):
    directory_name = "Expectation_From_Organization.eps"
    question = "What are your expectations from your organization?"


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/organization.csv")
    controller = ExpectationFromOrganizationFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)

