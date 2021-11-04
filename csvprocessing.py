import pandas as pd


def load_csv_data(file):
    '''
    Load CSV file in a pandas Dataframe
    '''
    data = pd.read_csv(file, low_memory=False)
    return data

