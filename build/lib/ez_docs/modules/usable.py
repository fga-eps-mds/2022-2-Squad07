import os
import glob
import argparse
from sys import argv, stdout
import importlib.resources
from ez_docs import cmd
import shutil


def verify_folder_output():
    # Check whether the specified path exists or not
    path = 'output/'
    exist = os.path.exists(path)
    if not exist:
        # Create a new directory because it does not exist
        os.makedirs(path)


def clean_dir_md():
    target_folder = 'output/'
    target_extension = 'md'
    # Find all the pathnames matching with the specified (target), according to the rules used by the Unix.
    target_file_names = glob.glob(target_folder + '*.' + target_extension)
    # Delete the files.
    for file_name in target_file_names:
        os.remove(file_name)
    os.remove('mdpdf.log')

def progress_bar(index: int, amount: int, char: str, final_length: int = 25):
    stdout.write("\033[F\033[K\033[F\033[K\033[F\033[K")
    print(f"\033[93m({index}/{amount})\033[0m {index * 100/amount: 1.2f}% [\033[96m", end='')
    charline = "".join([char for _ in range(round(final_length*index/amount))])
    print(charline + "\033[0m]")

def zipfolder(foldername, target_dir):            
    folder_to_zip = foldername
    output_zip = target_dir

    shutil.make_archive(output_zip, "zip", folder_to_zip)
    shutil.rmtree("output")
class CallCommand(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        #Catch the last argument given in the sys.arg
        command = argv[-1].lstrip('-')

        #Open the txt response
        path = importlib.resources.files(cmd)
        
        with open(file=f'{path}/{command}.txt', encoding='utf-8') as f:
           data = f.read()
           print(data)
        #Close the parser
        parser.exit()