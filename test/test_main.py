from ez_docs.main import mk_docs, main
import shutil
import os
import argparse

# "template.md example.csv name_idade"

example = {
    "template_directory": "test/template.md",
    "base_directory": "test/example.csv",
    "file_name_pattern": "nome_idade",
    "flag": 1,
    'zip': 0,
    "constraint": ""
}


def test_mk_docs():
    mk_docs(example)
    x = len(os.listdir('output'))
    shutil.rmtree('output')
    assert x == 4


def test_mk_docs_error():
    mk_docs(example)
    x = len(os.listdir('output'))
    shutil.rmtree('output')
    assert x != 3


def test_main(monkeypatch):
    def mock_parse_args(self):
        return argparse.Namespace(
            zip=0,
            flag=1,
            template_directory='template.md',
            base_directory='dados.csv', file_name_pattern='NOME_MATRICULA',
            _get_kwargs=lambda: {
                'flag': 1,
                'template_directory': 'test/template.md',
                'base_directory': 'test/example.csv',
                'file_name_pattern': 'nome_idade',
                'zip': 0,
                "constraint": ""
            }
        )
    monkeypatch.setattr(argparse.ArgumentParser, 'parse_args', mock_parse_args)
    main()
    x = len(os.listdir('output'))
    shutil.rmtree('output')
    assert x == 4


def test_main_error(monkeypatch):
    def mock_parse_args(self):
        return argparse.Namespace(
            flag=1,
            zip=0,
            template_directory='template.md',
            base_directory='dados.csv', file_name_pattern='NOME_MATRICULA',

            _get_kwargs=lambda: {
                'flag': 1,
                'template_directory': 'test/template.md',
                'base_directory': 'test/example.csv',
                'file_name_pattern': 'nome_idade',
                'zip': '0',
                "constraint": ""
            }
        )
    monkeypatch.setattr(argparse.ArgumentParser, 'parse_args', mock_parse_args)
    main()
    x = len(os.listdir('output'))
    shutil.rmtree('output')
    assert x != 3
