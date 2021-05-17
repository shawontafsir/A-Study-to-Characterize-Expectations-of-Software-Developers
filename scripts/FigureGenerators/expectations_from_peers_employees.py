import pandas as pd

from Base.FigureController import Controller


class ExpectationFromPeersEmployeesFigureController(Controller):
    figure_width = 6
    directory_name = "Expectation_From_Peers_Employees.eps"
    question = "What are your expectations from your peers and employees in the team?"
    # rename_category = {'Friendly': 'Supportive'}


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/peers_employees.csv")
    controller = ExpectationFromPeersEmployeesFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True, )
