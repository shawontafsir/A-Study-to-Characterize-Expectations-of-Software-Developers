import pandas as pd
import numpy as np
import scipy.stats as ss

def get_contingency_table(table, row_name, column_name):
    a = table.loc[row_name][column_name]
    b = table.loc[row_name].drop(columns=[column_name]).sum().sum()
    c = table.drop(index=[row_name])[column_name].sum().sum()
    d = table.drop(index=[row_name]).drop(columns=[column_name]).sum().sum()
    return np.array([[a,b],[c,d]])

def stat_test_manager():
    df = pd.read_csv("../../data/managers.csv")
    df['What is your Gender?'] = df['What is your Gender?'].map(lambda x: x if x.strip() == 'Male' else 'Female')
    gender = []
    career_opportunity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if any(item.strip() in ['Career Opportunities'] for item in
                   row[1]['categories'].strip().split(",")):
                career_opportunity.append(1)
            else:
                career_opportunity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "career": career_opportunity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender']=='Male']['career'], new_df[new_df['gender']=='Female']['career']))
    # contingency_table = pd.crosstab(new_df['gender'], new_df["career"])
    # print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Female', "Career Opportunity")))

def stat_test_team():
    df = pd.read_csv("../../data/managers.csv")
    gender = []
    team_player = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() == 'Team Player':
                team_player.append("Team Player")
            else:
                team_player.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "team": team_player
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df["team"])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Male', "Team Player")))


def stat_test_peer_employee():
    df = pd.read_csv("../../data/peers_employees.csv")
    df['What is your Gender?'] = df['What is your Gender?'].map(lambda x: x if x.strip() == 'Male' else 'Female')
    gender = []
    sincerity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if any(item.strip() in ['Sincerity', 'Supportive'] for item in
                   row[1]['categories'].strip().split(",")):
                sincerity.append(1)
            else:
                sincerity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "sincerity": sincerity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender']=='Male']['sincerity'], new_df[new_df['gender']=='Female']['sincerity']))

def stat_test_organization():
    df = pd.read_csv("../../data/organization.csv")
    df['What is your Gender?'] = df['What is your Gender?'].map(lambda x: x if x == 'Male' else 'Female')
    gender = []
    sincerity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'].strip() in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if any(item.strip() in ['Knack in Standard SE practice'] for item in row[1]['categories'].strip().split(",")):
                sincerity.append(1)
            else:
                sincerity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "sincerity": sincerity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender']=='Male']['sincerity'], new_df[new_df['gender']=='Female']['sincerity']))


def stat_test_government():
    df = pd.read_csv("../../data/government.csv")
    df['What is your Gender?'] = df['What is your Gender?'].map(lambda x: x if x == 'Male' else 'Female')
    gender = []
    sincerity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'].strip() in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if any(item.strip() in ['Career Opportunities'] for item in row[1]['categories'].strip().split(",")):
                sincerity.append(1)
            else:
                sincerity.append(0)

    new_df = pd.DataFrame({
        "gender": gender,
        "sincerity": sincerity
    })
    print(ss.mannwhitneyu(new_df[new_df['gender']=='Male']['sincerity'], new_df[new_df['gender']=='Female']['sincerity']))


def stat_test_university():
    df = pd.read_csv("../../data/government.csv")
    gender = []
    job = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() in ['Job Availability']:
                job.append('Job Availability')
            else:
                job.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "job": job
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df['job'])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Female', 'Job Availability')))
if __name__ == '__main__':
    stat_test_government()