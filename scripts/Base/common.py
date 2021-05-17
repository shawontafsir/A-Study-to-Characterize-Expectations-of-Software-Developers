import json


# def rename_header(dataframe):
#     temp_headers = json.load(open("../Data/Headers.json", "r"))
#     headers = {key: value['header'] for key, value in temp_headers.items()}
#     dataframe.rename(columns=headers, inplace=True)
#
#     return temp_headers

RQs = [
    "What are your expectations from your organization?",
    "What are your expectations from your manager?",
    "What are your expectations from the universities?",
    "What are your expectations from the new hires?",
    "What are your expectations from the Government?",
    "What are your expectations from your peers and employees in the team?"
]


def get_unique_categories():
    unique_categories = list()
    for rq in RQs:
        data = json.load(open("../data/category_wise_labels.json", "r"))
        for key, value in data.get(rq).items():
            if key not in unique_categories:
                unique_categories.append(key)

    return unique_categories


def get_category_wise_labels(question):
    data = json.load(open("../data/category_wise_labels.json", "r"))

    return data.get(question)
