from ez_docs.modules.data_cleaning import filter_data, find_delimiter
from ez_docs.modules.data_cleaning import filter_format
import pytest
import pandas as pd
import tempfile

final_data = [
    {'nome': 'Bruno', 'idade': '18'},
    {'nome': 'Miguel', 'idade': '18'},
    {'nome': 'Gobbi', 'idade': '18'},
    {'nome': 'Igor', 'idade': '18'},
]

final_data2 = [
    {'nome': 'Bruno', 'idade': '18'},
    {'nome': 'Miguel', 'idade': '18'},
    {'nome': 'Gobbi', 'idade': '18'},
    {'nome': 'Igor', 'idade': '18'},
    {'nome': 'Igor', 'idade': '18'},
]


def test_find_delimiter():
    assert find_delimiter("test/teams1.csv") == ","
    assert find_delimiter("test/teams2.csv") == ";"
    assert find_delimiter("test/teams3.csv") == "\\"
    assert find_delimiter("test/teams4.csv") == "~"


def test_data_cleaning():
    assert filter_data("test/example.csv") == final_data


def test_data_cleaning_error():
    assert filter_data("test/example.csv") != final_data2

def test_filter_format_csv():
    file_path = 'test/data.csv'
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    result_df = filter_format(file_path)
    
    assert result_df.equals(expected_df)

def test_filter_format_json():
    file_path = 'test/data.json'
    expected_df = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        
    result_df = filter_format(file_path)
        
    assert result_df.equals(expected_df)

def test_filter_format_invalid():
    file_path = 'data.txt'
    
    with pytest.raises(ValueError):
        filter_format(file_path)
