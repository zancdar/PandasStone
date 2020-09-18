import numpy as np
import pandas as pd

if __name__ == '__main__':
    hscards = pd.read_json("cards.collectible.json")
    extensions = pd.read_csv("extensions_info.csv", sep=';')
    hscards = pd.merge(hscards, extensions, how='left', on='set')
    print(hscards.head())

    # print(hscards.pivot_table('id', index='cardClass', columns='type', aggfunc=pd.Series.count))
    # print(hscards.columns)
    # print(hscards.pivot_table('id', index='set', aggfunc=pd.Series.count))
