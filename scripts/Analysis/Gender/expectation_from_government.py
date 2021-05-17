import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from FigureGenerators.expectation_from_universities import ExpectationFromUniversityFigureController
from Base.FigureController import Controller
from FigureGenerators.expectation_from_government import ExpectationFromGovernmentFigureController
from FigureGenerators.expectation_from_managers import ExpectationFromManagersFigureController
from FigureGenerators.expectation_from_new_hires import ExpectationFromNewHiresFigureController
from FigureGenerators.expectation_from_organization import ExpectationFromOrganizationFigureController
from FigureGenerators.expectations_from_peers_employees import ExpectationFromPeersEmployeesFigureController
from FigureGenerators.expectations_from_peers_employees import ExpectationFromPeersEmployeesFigureController

def short_word(text):
    text = text.strip()
    if len(text.split(" ")) >= 2:
        return ''.join([item[0] for item in text.lower().split(" ")]).upper()
    else:
        return text


def show_stats(df, class_name):
    question = 'What is your Gender?'
    df[question] = df[question].map(lambda x: x.split(";")[-1])
    df[question] = df[question].map(lambda x: x if x == 'Male' else 'Female')
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

    for key in all_keys:
        print(key + " = " + short_word(key) + ", ", end='')
    print("\n")
    for key in all_keys:
        print(short_word(key) + " (\%)" + " & ", end='')
    print("\n")
    for role in unique_roles:
        print(role + " & ", end='')
        for i in range(len(all_keys)-1):
            print(str(round(plot_data[role][i], 2)) + " & ", end='')
        print(str(round(plot_data[role][i], 2)) + " \\\\")

def print_stats(df, class_name):
    question = 'What is your Gender?'
    df[question] = df[question].map(lambda x: x.split(";")[-1])
    df[question] = df[question].map(lambda x: x if x == 'Male' else 'Female')
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

    for j, role in enumerate(unique_roles):
        print(str(j + 1) + ") \\textbf{" + role + "}: ", end="")
        for i, key in enumerate(all_keys):
            print(short_word(key) + " (" + str(round(plot_data[role][i], 2)) + "\\%), ", end="")

    # for key in all_keys:
    #     print(key + " = " + short_word(key) + ", ", end='')
    # print("\n")
    # for key in all_keys:
    #     print(short_word(key) + " (\%)" + " & ", end='')
    # print("\n")
    # for role in unique_roles:
    #     print(role + " & ", end='')
    #     for i in range(len(all_keys)-1):
    #         print(str(round(plot_data[role][i], 2)) + " & ", end='')
    #     print(str(round(plot_data[role][i], 2)) + " \\\\")

def show_bar_plot(df, class_name):
    controller_male = class_name(df[df['What is your Gender?'] == 'Male'])
    controller_female = class_name(df[df['What is your Gender?'] == 'Female'])
    controller_female.process_data()
    controller_male.process_data()
    all_keys = sorted(set().union(controller_male.plot_data.keys(), controller_female.plot_data.keys()))
    total_male_data = len(df[df['What is your Gender?'] == 'Male'])
    total_female_data = len(df[df['What is your Gender?'] == 'Female'])
    male_data = []
    female_data = []
    for item in all_keys:
        male_data.append(controller_male.plot_data.get(item, 0))
        female_data.append(controller_female.plot_data.get(item, 0))
    male_data = (np.array(male_data) / total_male_data) * 100
    female_data = (np.array(female_data) / total_female_data) * 100
    barWidth = 0.25
    r1 = np.arange(len(all_keys))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, male_data, color='#7f6d5f', width=barWidth, edgecolor='white', label='Male')
    plt.bar(r2, female_data, color='#557f2d', width=barWidth, edgecolor='white', label='Female')

    # Add xticks on the middle of the group bars
    # plt.xlabel('group', fontweight='bold')
    plt.ylabel('Frequency (%)', fontsize=32)
    plt.xticks([r + barWidth for r in range(len(all_keys))], all_keys)

    # Create legend & Show graphic
    plt.legend(prop={'size': 32})
    plt.show()
if __name__ == '__main__':
    # Load Data #
    # df = pd.read_csv("../../data/government.csv")
    # # # show_bar_plot(df, ExpectationFromGovernmentFigureController)
    # print_stats(df, ExpectationFromGovernmentFigureController)


    # df = pd.read_csv("../../data/managers.csv")
    # print_stats(df, ExpectationFromManagersFigureController)
    # show_bar_plot(df, ExpectationFromManagersFigureController)
    # show_stats(df, ExpectationFromManagersFigureController)
    #
    #
    # df = pd.read_csv("../../data/new_hires.csv")
    # # show_bar_plot(df, ExpectationFromNewHiresFigureController)
    # print_stats(df, ExpectationFromNewHiresFigureController)
    #
    #
    df = pd.read_csv("../../data/organization.csv")
    # show_bar_plot(df, ExpectationFromOrganizationFigureController)
    print_stats(df, ExpectationFromOrganizationFigureController)
    #
    #
    # df = pd.read_csv("../data/peers.csv")
    # show_bar_plot(df, ExpectationFromPeersFigureController)
    # show_stats(df, ExpectationFromGovernmentFigureController)
    #
    #
    # df = pd.read_csv("../../data/peers_employees.csv")
    # show_bar_plot(df, ExpectationFromPeersEmployeesFigureController)
    # print_stats(df, ExpectationFromPeersEmployeesFigureController)
    #
    #
    # df = pd.read_csv("../../data/universities.csv")
    # # show_bar_plot(df, ExpectationFromGovernmentFigureController)
    # print_stats(df, ExpectationFromUniversityFigureController)


# female manager career opportunity
# male manager team player
#female peer employee sincerity, supportive
# female university job availability