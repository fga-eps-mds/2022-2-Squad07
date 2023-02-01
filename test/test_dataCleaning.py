from ez_docs.modules.data_cleaning import filter_data, find_delimiter

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