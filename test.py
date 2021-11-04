import pandas as pd

import pytest

from csvprocessing import load_csv_data

from unittest.mock import patch



def _load_test_data():
    data = pd.DataFrame([[0, 2, 7, 4, 8],
                         [1, 7, 6, 3, 7],
                         [1, 1, "None", 8, 9],
                         [0, 2, 3, "None", 6],
                         [0, 5, 1, 4, 9]], 
                        columns = [f"feature_{i}" if i!=0 
                                  else "class" for i in range(5)])
    return data



@patch('csvprocessing.pd.read_csv')
def test_load_csv_data(load_csv_data):   
    pass