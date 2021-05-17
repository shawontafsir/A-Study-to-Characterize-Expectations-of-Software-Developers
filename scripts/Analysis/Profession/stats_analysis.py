import pandas as pd
import numpy as np
import scipy.stats as ss

def get_contingency_table(table, row_name, column_name):
    a = table.loc[row_name][column_name]
    b = table.loc[row_name].drop(columns=[column_name]).sum().sum()
    c = table.drop(index=[row_name])[column_name].sum().sum()
    d = table.drop(index=[row_name]).drop(columns=[column_name]).sum().sum()
    return np.array([[a,b],[c,d]])




def stat_new_hires():
    df = pd.read_csv("../../data/new_hires.csv")
    gender = []
    career_opportunity = []
    for row in df.iterrows():
        if row[1]['For how many years have you coded professionally?'] in ['less than 2', '2 to 5']:
            gender.append('0-5')
        else:
            gender.append('>5')
        if row[1]['categories'].strip() == 'Knack in Standard SE practice':
            career_opportunity.append(1)
        else:
            career_opportunity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "career": career_opportunity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender'] == '0-5']['career'], new_df[new_df['gender'] == '>5']['career']))


def stat_organization():
    df = pd.read_csv("../../data/organization.csv")
    gender = []
    career_opportunity = []
    for row in df.iterrows():
        if row[1]['For how many years have you coded professionally?'] in ['less than 2', '2 to 5']:
            gender.append('0-5')
        else:
            gender.append('>5')
        if row[1]['categories'].strip() == 'Work Benefits':
            career_opportunity.append(1)
        else:
            career_opportunity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "career": career_opportunity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender'] == '>5']['career'], new_df[new_df['gender'] == '0-5']['career']))


def stat_peers1():
    df = pd.read_csv("../../data/peers_employees.csv")
    gender = []
    career_opportunity = []
    for row in df.iterrows():
        if row[1]['For how many years have you coded professionally?'] in ['less than 2', '2 to 5']:
            gender.append('0-5')
        else:
            gender.append('>5')
        if row[1]['categories'].strip() == 'Supportive attitude':
            career_opportunity.append(1)
        else:
            career_opportunity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "career": career_opportunity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender'] == '>5']['career'], new_df[new_df['gender'] == '0-5']['career']))

if __name__ == '__main__':
    stat_peers1()