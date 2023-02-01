import argparse
import time
from ez_docs.modules.doc_generation import doc_generator
from ez_docs.modules.usable import *
from ez_docs.modules.data_cleaning import filter_data

def mk_docs(dict_args: dict):
    verify_folder_output()
    dataset = filter_data(dict_args['base_directory'])
    initial_time = time.time()
    for index in range(len(dataset)):
        doc_generator(
            dict_args['template_directory'],
            dataset[index], dict_args['file_name_pattern'],
            dict_args['flag']
        )
        progress_bar(index + 1, len(dataset), '#')
        
    print(f"Done.\nTotal generated objects: {len(dataset)}")
    print(f"Elapsed time: {time.time() - initial_time : 1.2f}s")
        

    if dict_args['flag'] == '1':
        clean_dir_md()

    if dict_args['zip'] == '1':
        print("Zipping files")
        zipfolder("output", "output")

def main():
    parser = argparse.ArgumentParser(description='Documents auto-generated.', add_help=False)
    parser.add_argument('--about', nargs=0, help='About our project', action=CallCommand)
    parser.add_argument('--architecture', nargs=0, help='Architecture stuff', action=CallCommand)
    parser.add_argument('--help', nargs=0, help='How to use it', action=CallCommand)
    parser.add_argument('--list', nargs=0, help='Command list', action=CallCommand)
    parser.add_argument('--flag', help='Flag to output file extension. 0 for .md, 1 for .pdf', default='1')
    parser.add_argument('--zip', help='Define if the output folder is compacted. 1 for yes, 0 for no.', default='0')
    parser.add_argument('template_directory', help='Template dictionary.')
    parser.add_argument('base_directory', help='Database directory.')
    parser.add_argument('file_name_pattern', help='Output file pattern name.')
    args = parser.parse_args()
    mk_docs(dict(args._get_kwargs()))


if __name__ == '__main__':
    main()
