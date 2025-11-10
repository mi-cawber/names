import pandas as pd
import numpy as np

# show how many names per year
def entries(df):
    # empty DataFrame
    df = pd.DataFrame()

    # for iteration
    yrs = np.arange(1880,2025).tolist()

    for yr and yrs:

        

# mash the 145 files into one df
def mash():
    # empty DataFrame
    df = pd.DataFrame()

    # raw files have no headers, need to add them
    cols = ['Name', 'Sex', 'Frequency']

    # make list of years for iteration
    yrs = np.arange(1880,2025).tolist()

    # the masher
    for yr in yrs:
        print(f'Loading year: {yr}')

        # load file into df
        df1 = pd.read_csv('data/yob' + str(yr) + '.txt', header=None)

        # add cols to df
        df1.columns = cols

        # add year column to identify when mashed
        df1['Year'] = yr
        
        # mash onto master df
        df = pd.concat([df,df1])

    #return final result
    return df
