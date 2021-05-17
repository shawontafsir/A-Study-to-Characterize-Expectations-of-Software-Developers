import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from Base.FigureController import Controller
from FigureGenerators.expectation_from_government import ExpectationFromGovernmentFigureController
from FigureGenerators.expectation_from_managers import ExpectationFromManagersFigureController
from FigureGenerators.expectation_from_new_hires import ExpectationFromNewHiresFigureController
from FigureGenerators.expectation_from_organization import ExpectationFromOrganizationFigureController
from FigureGenerators.expectation_from_new_hires import ExpectationFromNewHiresFigureController
from FigureGenerators.expectations_from_peers_employees import ExpectationFromPeersEmployeesFigureController


def show_bar_plot(df, class_name):
    question = 'What is your current role?'
    df[question] = df[question].map(lambda x: x.split(";")[-1])
    # df1 = df.groupby([question,'categories']).agg(['count'])
    # ax = df1.plot(kind='bar', figsize=(10,6), color="indigo", fontsize=13)
    # ax.set_alpha(0.8)
    # ax.set_title("My Bar Plot", fontsize=22)
    # ax.set_ylabel("Some Heading on Y-Axis", fontsize=15);
    # plt.show()
    unique_roles = df[question].unique()
    controller_role = dict()
    key_item = []
    for role in unique_roles:
        temp = class_name(df[df[question] == role])
        temp.process_data()
        key_item.extend(list(temp.plot_data.keys()))
        controller_role[role] = temp

    all_keys = sorted(set(key_item))
    total_count = {}
    for role in unique_roles:
        total_count[role] = len(df[df[question] == role])


    plot_data = {role: [] for role in unique_roles}

    for key in all_keys:
        for role in unique_roles:
            plot_data[role].append(controller_role[role].plot_data.get(key,0))


    for role in unique_roles:
        plot_data[role] = (np.array(plot_data[role]) / total_count[role]) * 100


    barWidth = 0.5
    ranges = []
    ranges.append(np.arange(len(all_keys)))
    for i in range(1, len(unique_roles)):
        temp = [x + barWidth for x in ranges[-1]]
        ranges.append(temp)

    plt.rcParams["figure.figsize"] = (20, 3)
    for i, role in enumerate(unique_roles):
        plt.bar(ranges[i], plot_data[role], width=barWidth, edgecolor='white', label=role)



    plt.ylabel('Frequency (%)', fontsize=32)
    plt.xticks([r + barWidth for r in range(len(all_keys))], all_keys, rotation=45,fontsize=16)

    # Create legend & Show graphic
    plt.legend(prop={'size': 32})
    plt.show()
if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../../data/government.csv")
    show_bar_plot(df, ExpectationFromGovernmentFigureController)


    # df = pd.read_csv("../../data/managers.csv")
    # show_bar_plot(df, ExpectationFromManagersFigureController)
    #
    #
    # df = pd.read_csv("../../data/new_hires.csv")
    # show_bar_plot(df, ExpectationFromNewHiresFigureController)
    #
    #
    # df = pd.read_csv("../../data/organization.csv")
    # show_bar_plot(df, ExpectationFromOrganizationFigureController)
    #
    #
    # df = pd.read_csv("../../data/peers_employees.csv")
    # show_bar_plot(df, ExpectationFromPeersEmployeesFigureController)
    #
    #
    # df = pd.read_csv("../../data/universities.csv")
    # show_bar_plot(df, ExpectationFromGovernmentFigureController)


# female manager career opportunity
# male manager team player
#female peer employee sincerity, supportive
# female university job availability