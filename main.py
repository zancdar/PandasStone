import numpy as np
import pandas as pd

def askCriterias(df):
    df = askStandard(df)
    criterias = {}
    while True:
        print(df.columns)
        col = input("Which column to filter ? (S to stop)")
        if col in ('s', 'S'):
            break
        elif col in df.columns:
            print(df[col].unique())
            value = input("What value ? 1 or more separated by space")
            value = value.split(sep=' ')
            if(checkValues(value, df[col].unique())):
                criterias[col] = value
        else:
            print("This column do not exist !")

        for i, j in criterias.items():
            df = df.loc[df[i].isin(j)]

    return df


def askStandard(df):
    while True:
        ans = input("Standard uniquement ? O/N")
        if ans in ('O', 'o'):
            return df.loc[df['mode'] == 'STANDARD']
        elif ans in ('N', 'n'):
            return df

def checkValues(values, available):
    for i in values:
        if i not in available:
            print("La valeur ", i, " n'est pas valide !")
            return False
    return True


if __name__ == '__main__':

    # Opening sources
    hscards = pd.read_json("cards.collectible.json")
    extensions = pd.read_csv("extensions_info.csv", sep=';')

    # Merge sources
    hscards = pd.merge(hscards, extensions, how='left', on='set')

    #pandas options
    pd.set_option('display.max_columns', None)

    #cleaning datas
    hscards.dropna(subset=['cost'], how='all', inplace=True) #drop cost=Nan
    hscards = hscards.explode('mechanics')

    # Doing stuff
    rslt_df = askCriterias(hscards)
    print(pd.pivot_table(rslt_df, values='id', index='cardClass', columns='type', aggfunc=pd.Series.count))

    # print(pd.pivot_table(hscards, values='id', index='title_fr', columns='mode', aggfunc=pd.Series.count))

    # print(hscards.pivot_table('id', index='cardClass', columns='type', aggfunc=pd.Series.count))
    # print(hscards.columns)
    # rslt_df = hscards.loc[hscards['mode'] == 'STANDARD']
    # rslt_df = hscards.loc[(hscards['type'] == 'HERO') & (hscards['mode'] == 'STANDARD') & (hscards['cardClass'].isin(['MAGE', 'WARRIOR']))]
    # print(rslt_df)

    # rslt_df = hscards.loc[hscards['cost'].isna()]
    # print(rslt_df['name'])
    # for index, row in rslt_df.iterrows():
    #     print(row['name'], " ", row['title_fr'])

    # print(pd.pivot_table(rslt_df, values='id', index='cardClass', columns='type', aggfunc=pd.Series.count))
    # print(pd.pivot_table(rslt_df, values='id', index=['title_fr','cardClass'], columns='type', aggfunc=pd.Series.count))
    # pivot = pd.pivot_table(rslt_df, values='id', index=['cardClass', 'title_fr'], columns='type', aggfunc=pd.Series.count)
    # print(type(pivot))
    # pd.set_option('display.max_rows', pivot.shape[0]+1)


