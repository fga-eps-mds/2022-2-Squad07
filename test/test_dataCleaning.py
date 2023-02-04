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


def test_filter_format():
    # Test with a CSV file
    with tempfile.NamedTemporaryFile(
        mode='w',
        delete=False,
        suffix='.csv'
    ) as temp:

        temp.write("col1,col2\n1,2\n3,4")
        temp.seek(0)
        result = filter_format(temp.name)
        assert isinstance(result, pd.DataFrame)

    # Test with a JSON file
    with tempfile.NamedTemporaryFile(
        mode='w',
        delete=False,
        suffix='.json'
    ) as temp:
        temp.write('{"col1": [1, 3], "col2": [2, 4]}')
        temp.seek(0)
        result = filter_format(temp.name)
        assert isinstance(result, pd.DataFrame)

    # Test with an invalid extension
    location = "path/to/invalid/file.invalid"
    with pytest.raises(Exception):
        filter_format(location)
