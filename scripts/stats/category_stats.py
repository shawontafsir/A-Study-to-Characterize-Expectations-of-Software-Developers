import pandas as pd

from Base.common import get_unique_categories, RQs, get_category_wise_labels


def get_categories_count_from_labels(df, question, category):
    labels_column = list(df['labels'])
    category_wise_labels = get_category_wise_labels(question)
    nc, nr = 0, 0
    for row in labels_column:
        row_wise_category = list()
        for label in row.split(', '):
            for key, val in category_wise_labels.items():
                if label in val and key == category:
                    row_wise_category.append(key)

        nc += len(row_wise_category)
        nr += min(1, len(row_wise_category))

    return nc, nr


def get_category_and_response_number(category):
    result = dict()
    total_cat, total_res = 0, 0

    df = pd.read_csv('../data/organization.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from your organization?", category)
    result["organization"] = dict(NC=nc, NR=nr)
    total_cat += nc
    total_res += nr

    df = pd.read_csv('../data/managers.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from your manager?", category)
    result["manager"] = dict(NC=nc, NR=nr)
    total_cat += nc
    total_res += nr

    df = pd.read_csv('../data/peers_employees.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from your peers and employees in the team?", category)
    result["peers_employees"] = dict(NC=nc, NR=nr)
    total_cat += nc
    total_res += nr

    df = pd.read_csv('../data/new_hires.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from the new hires?", category)
    result["new_hires"] = dict(NC=nc, NR=nr)
    total_cat += nc
    total_res += nr

    df = pd.read_csv('../data/government.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from the Government?", category)
    result["govt_uni"] = dict(NC=nc, NR=nr)
    total_cat += nc
    total_res += nr

    df = pd.read_csv('../data/universities.csv')
    nc, nr = get_categories_count_from_labels(df, "What are your expectations from the universities?", category)
    result["govt_uni"]['NC'] += nc
    result["govt_uni"]['NR'] += nr
    total_cat += nc
    total_res += nr

    return result, total_cat, total_res

well = ["Work Benefits", "Work-place culture", "People skill", "Sincerity", "Supportive attitude"]
prod = ["Goal Achievement", "Tech Savvy"]
grow = ["Career Opportunities", "Learning Opportunities", "Career support"]
lead = ["Proper Management", "Policy and facility", "Support for industry"]
prac = ["Knack in Standard SE practice", "Industry oriented teaching", "Motivation for Learning",
        "Proper Education", "Learning Environment"]


if __name__ == "__main__":
    unique_categories = get_unique_categories()
    total = dict()
    # rem = unique_categories - well - prod - grow - lead - prac
    rem = [c for c in unique_categories if c not in well]
    rem = [c for c in rem if c not in prod]
    rem = [c for c in rem if c not in grow]
    rem = [c for c in rem if c not in lead]
    rem = [c for c in rem if c not in prac]

    for cat in unique_categories:
        data, total_cat, total_res = get_category_and_response_number(cat)
        if 'total_cat' not in total:
            total['total_cat'] = total_cat
            total['total_res'] = total_res
        else:
            total['total_cat'] += total_cat
            total['total_res'] += total_res

        row = "\\bf{" + cat + "}"
        for k, v in data.items():
            if k not in total:
                total[k] = dict(NC=0, NR=0)

            if v['NC']:
                row += " & {} & {}".format(v['NC'], v['NR'])
                total[k]['NC'] += v['NC']
                total[k]['NR'] += v['NR']
            else:
                row += " &   & "
        row += " & " + str(total_cat) + " & " + str(total_res) + " \\\\ \\cmidrule{2-13}"
        print(row)

    total_row = "\\bf{Total}"
    for k, v in total.items():
        if k not in ("total_cat", "total_res"):
            total_row += " & {} & {}".format(v['NC'], v['NR'])

    total_row += " & " + str(total['total_cat']) + " & " + str(total['total_res']) + " \\\\ \\midrule"
    print(total_row)
