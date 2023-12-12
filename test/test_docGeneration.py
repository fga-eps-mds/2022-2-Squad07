from ez_docs.modules.doc_generation import loc_sub, verify_patterns
from ez_docs.modules.doc_generation import slugify
from ez_docs.modules.doc_generation import recognize_file_name

key_value = {
    "NOME": "Wallace",
    "MATRICULA": "20990088"
}

def test_verify_patterns():
    assert verify_patterns(["$$key$$", "{[(key)]}"]) == True
    assert verify_patterns(["$$key$$", ":{key}:", "?-key-?"]) == True
    assert verify_patterns(["&%key&%"]) == False
    assert verify_patterns(["-->keykey<--"]) == False
    assert verify_patterns("<<<keys>>>") == False

def test_loc_sub():
    assert loc_sub("Ola <<Chave>>", "Chave", "Mundo") == "Ola Mundo"


def test_loc_sub_error():
    assert loc_sub("Ola <<Chave>>", "Chave", "Mundo") != "Ola Mudo"


def test_slugify():
    assert slugify("bruno#o:brabo. mago") == "brunoobrabo-mago"


def test_slugify_error():
    assert slugify("bruno#o:brabo. mago") != "bruno#o:brabo. mago"


def test_recognize_file_name():
    assert (
        recognize_file_name(key_value, "NOME_MATRICULA")
        ==
        "wallace_20990088"
    )


def test_recognize_file_name_error():
    assert (
        recognize_file_name(key_value, "NOME_MATRICULA")
        !=
        "Wallace_20990088"
    )
