import pandas as pd

import pytest

from csvprocessing.csvprocessing import (
    load_csv_data,
    calculate_percentile_for_column,
    get_records_above,
    check_data_type
)

#from unittest.mock import patch



def _load_test_data():
    data = pd.DataFrame([[0, 2, 7, 4, 8],
                         [1, 7, 6, 3, 7],
                         [1, 1, "None", 8, 9],
                         [0, 2, 3, "None", 6],
                         [0, 5, 1, 4, 9]], 
                        columns = [f"feature_{i}" if i!=0 
                                  else "class" for i in range(5)])
    return data


#@patch('csvprocessing.pd.read_csv')
# def test_load_csv_data(load_csv_data):   
#     pass


@pytest.mark.parametrize("column, ref_percentile, val_expected", [("feature_1", 0.9, 6.2)])
def test_percentil_for_column(column, ref_percentile, val_expected):   
    data = _load_test_data()
    expected = val_expected
    result = calculate_percentile_for_column(data, column, ref_percentile)
    assert expected == result


@pytest.mark.parametrize("column, ref_value, val_expected", [("feature_1", 6.2, '[{"class":1,"feature_1":7,"feature_2":6,"feature_3":3,"feature_4":7}]')])
def test_get_records_above(column, ref_value, val_expected):
    '''
    Test function get_records_above
    '''
    data = _load_test_data()
    expected = val_expected
    result = get_records_above(data, column, ref_value)
    assert expected == result


@pytest.mark.parametrize("column, types", [("feature_1", ["int64", "float64"])])
def test_type_data_check(column, types):   
    data = _load_test_data()
    result = check_data_type(data, column, types)
    assert result == True
