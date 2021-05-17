from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np

from Base.common import get_category_wise_labels


class Controller(object):
    xlabel = "Frequency (%)"
    ylabel = ""
    x_tick_size = 40
    y_tick_size = 40
    title = None
    directory_name = None
    axis_title_size = 40
    title_size = 20
    prop_size = 25
    extension = 'eps'
    palette = "Set2"
    figure_height = 20
    figure_width = 10
    plot_data = None
    rename_category = dict()
    question = None
    category_wise_labels = None

    # palettes = ["deep", "muted", "pastel", "bright", "dark", "colorblind"]

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.num_of_respondents = len(dataframe)
        self.category_wise_labels = get_category_wise_labels(self.question)
        self.root = "../Figures/"
        rcParams.update({'figure.autolayout': True})
        sns.set_palette(self.palette)
        sns.set_context("paper")
        self.fig, self.ax = plt.subplots(figsize=(self.figure_height, self.figure_width))
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        plt.xticks(fontsize=self.x_tick_size)
        plt.yticks(fontsize=self.y_tick_size)

    def get_categories_from_labels(self):
        li = list(self.dataframe['labels'])
        categories = list()
        for value in li:
            row_wise_category = list()
            for v in value.split(', '):
                for key, val in self.category_wise_labels.items():
                    if v in val and key not in row_wise_category:
                        row_wise_category.append(key)
            categories.extend(row_wise_category)

        return categories

    # def get_categories(self):
    #     li = list(self.dataframe['categories'])
    #     categories_list = list()
    #     for value in li:
    #         for v in value.split(', '):
    #             categories_list.append(self.rename_category.get(v, v))
    #
    #     return categories_list

    def get_unique_categories(self):
        categories_list = self.get_categories_from_labels()
        unique = list()
        for category in categories_list:
            if category not in unique:
                unique.append(category)

        return unique

    def set_dataframe(self, new_dataframe):
        self.dataframe = new_dataframe

    def process_data(self, **kwargs):
        plot_data = dict()

        for item in self.get_categories_from_labels():
            if item in plot_data:
                plot_data[item] += 1
            else:
                plot_data[item] = 1

        self.plot_data = plot_data

    @staticmethod
    def formatted_response_percentages(options_list, frequency_list):
        response_percentage = ''
        for i in range(1, len(options_list) + 1):
            response_percentage += '{}) {} {}\\%, '.format(i, options_list[i - 1], round(frequency_list[i - 1], 2))

        response_percentage = response_percentage[:-2] if response_percentage else response_percentage

        return response_percentage

    def draw_figure(self, save=False, legend=False, **kwargs):
        if self.xlabel is None:
            print("Attention !!! xlabel not set")
            return
        else:
            plt.xlabel(self.xlabel, fontsize=self.axis_title_size)
        if self.ylabel is None:
            print("Attention !!! ylabel not set")
            return
        else:
            plt.ylabel(self.ylabel, fontsize=self.axis_title_size)

        plt.autoscale(True)
        if legend:
            plt.legend(loc='upper left', prop={'size': self.prop_size})

        if self.title is not None:
            plt.title(self.title, fontsize=self.title_size)
        if save:
            if self.directory_name is None:
                print("Attention !!! directory name not set")
            else:
                plt.savefig(self.root + self.directory_name, format=self.extension, dpi=5000)
        else:
            plt.show()

    def draw_figure_bar_horizontally(self, save=False, legend=False, **kwargs):
        alpha = kwargs.get('alpha', 0.5)
        height = kwargs.get('height', 0.35)
        align = kwargs.get('align', 'center')
        if 'exclude_fields' in kwargs:
            for data in kwargs['exclude_fields']:
                del self.plot_data[data]

        self.plot_data = {k: v for k, v in sorted(self.plot_data.items(), key=lambda item: item[1])}
        objects = self.plot_data.keys()
        data_objects = np.arange(len(objects))
        frequency = list(self.plot_data.values())
        frequency_percentage = [rf * 100 / self.num_of_respondents for rf in frequency]

        print(self.formatted_response_percentages(list(objects), frequency_percentage))

        plt.barh(data_objects, frequency_percentage, align=align, alpha=alpha, height=height, color="grey")
        plt.yticks(data_objects, objects)

        # Add annotation to bars
        patches = self.ax.patches
        for i in range(len(patches)):
            plt.text(patches[i].get_width() + 0.2, patches[i].get_y() + 0.1,
                     str(round(frequency[i], 2)), fontsize=30,
                     fontweight='bold', color='black')

        self.draw_figure(save=save)

    def draw_figure_bar_vertically(self, save=False, legend=False, **kwargs):
        alpha = kwargs.get('alpha', 0.5)
        align = kwargs.get('align', 'center')
        width = kwargs.get('width', 0.35)
        if 'exclude_fields' in kwargs:
            for field in kwargs['exclude_fields']:
                del self.plot_data[field]

        self.plot_data = {k: v for k, v in sorted(self.plot_data.items(), key=lambda item: item[1])}
        objects = self.plot_data.keys()
        data_objects = np.arange(len(objects))
        frequency = self.plot_data.values()
        frequency = [af * 100 / self.num_of_respondents for af in frequency]

        print(self.formatted_response_percentages(list(objects), frequency))

        plt.bar(data_objects, frequency, align=align, alpha=alpha, width=width, color="grey")
        plt.xticks(data_objects, objects)
        plt.xticks(rotation=90)

        self.draw_figure(save=save)
