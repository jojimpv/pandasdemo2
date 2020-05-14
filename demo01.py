"""
Data import
https://github.com/tategallery/collection
"""
import sys
import time
import pandas as pd
import sqlite3

csv_file = '/Users/jojivarghese/works/data/artwork_data.csv'
selected_columns = ['id', 'artist', 'title', 'medium', 'year',
                    'acquisitionYear', 'height', 'width', 'units']


def main():
    df = pd.read_csv(csv_file, index_col='id', usecols=selected_columns)
    df = df.iloc[1:1000, :].copy()
    print(df)
    df.sample(5).index
    df.drop(df.sample(5).index)
    # pd.merge(df1, df2, how='left', left_index=True, right_on='playID', indicator=True)
    # pd.merge(df1, df2, validate='1:1')
    df[df['artist'].str.endswith('Robert')]
    # pd.merge(df1, df2, left_on=['a','b'], right_on=['a', 'b'])
    # df.filter(like='art')
    # df1.join([df2, df3])  # using common indexes not columns
    idx = pd.IndexSlice
    df.sort_index()
    df.loc[idx[1039:1044], :]


if __name__ == '__main__':
    t01 = time.time()
    main()
    t02 = time.time()
    print(f'{sys.argv[0]} took {t02 - t01:.0f} seconds')
