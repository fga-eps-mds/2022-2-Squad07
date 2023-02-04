from ez_docs.modules.usable import progress_bar, zipfolder, clean_dir_md
import shutil
import glob
import os


def test_progress_bar(capsys):
    progress_bar(4, 10, "#", 10)
    out, err = capsys.readouterr()
    out = out[
        len("\x1b[93m(1/10)\x1b[0m  10.00% [\x1b[96m"): -len("\x1b[0m]\n")
    ]
    assert out == "####"


def test_progress_bar_error(capsys):
    progress_bar(8, 10, "#", 10)
    out, err = capsys.readouterr()
    out = out[
        len("\x1b[93m(1/10)\x1b[0m  10.00% [\x1b[96m"): -len("\x1b[0m]\n")
    ]
    assert out != "#####"


def test_zipfolder():
    foldername = "testing_folder"
    target_dir = "test_zip"

    # Create a test folder
    os.makedirs(foldername)
    os.makedirs('output')

    # Call the zipfolder function
    zipfolder(foldername, target_dir)

    # Check if the zip file was created
    assert os.path.exists(target_dir + ".zip")

    # Clean up
    os.remove(target_dir + ".zip")
    shutil.rmtree(foldername)


def test_clean_dir_md():

    os.makedirs('output')

    # Create some test .md files
    with open("output/test1.md", "w") as f:
        f.write("Test content")
    with open("output/test2.md", "w") as f:
        f.write("Test content")
    with open("mdpdf.log", "w") as f:
        f.write("Test log content")

    # Call the clean_dir_md function
    clean_dir_md()

    # Check if the files and the log were deleted
    assert not glob.glob("output/*.md")
    assert not os.path.exists("mdpdf.log")
