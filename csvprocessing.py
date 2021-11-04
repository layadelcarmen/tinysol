import pandas as pd


def load_csv_data(file):
    '''
    Load CSV file in a pandas Dataframe
    '''
    data = pd.read_csv(file, low_memory=False)
    return data


def calculate_percentile_for_column(df, column, ref_percentile):
    '''
    Calculate the percentile for the specified column in a Dataframe
    '''    
    return df[column].quantile(ref_percentile)


def get_records_above(df, column, val_percentile):
    '''
    Get the records above a certain value in the specified Dataframe´s column 
    '''     
    return df[df[column] > val_percentile].to_json(orient='records')
