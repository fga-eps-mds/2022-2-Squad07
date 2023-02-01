from ez_docs.modules.doc_generation import *

key_value = {
    "NOME": "Wallace",
    "MATRICULA": "20990088"
}

def test_loc_sub():
    assert loc_sub("Ola <<Chave>>", "Chave", "Mundo")  == "Ola Mundo"

def test_loc_sub_error():
    assert loc_sub("Ola <<Chave>>", "Chave", "Mundo")  != "Ola Mudo"

def test_slugify():
    assert slugify("bruno#o:brabo. mago") == "brunoobrabo-mago"

def test_slugify_error():
    assert slugify("bruno#o:brabo. mago") != "bruno#o:brabo. mago"

def test_recognize_file_name():
    assert recognize_file_name(key_value, "NOME_MATRICULA") == "wallace_20990088"

def test_recognize_file_name_error():
    assert recognize_file_name(key_value, "NOME_MATRICULA") != "Wallace_20990088"