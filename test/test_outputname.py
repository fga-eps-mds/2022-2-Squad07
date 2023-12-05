from ez_docs.main import mk_docs, main
import shutil
import os
import argparse

def test_output_folder_name(monkeypatch):
    def mock_parse_args(self):
        return argparse.Namespace(
            zip=0,
            flag=1,
            template_directory='template.md', output_folder='example3',
            base_directory='example.csv', file_name_pattern='NOME_MATRICULA',
            _get_kwargs=lambda: {
                'flag': 1,
                'output_folder': "example3",
                'template_directory': 'test/template.md',
                'base_directory': 'test/example.csv',
                'file_name_pattern': 'nome_idade',
                'zip': 0,
                "constraint": ""
            }
        )
    monkeypatch.setattr(argparse.ArgumentParser, 'parse_args', mock_parse_args)
    main()
    shutil.rmtree('output')
    assert os.path.isdir("example2")