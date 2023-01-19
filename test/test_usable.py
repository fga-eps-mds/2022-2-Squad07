from ez_docs.modules.usable import*

def test_progress_bar(capsys):
    progress_bar(4, 10, "#", 10)
    out, err = capsys.readouterr()
    out = out[len("\x1b[93m(1/10)\x1b[0m  10.00% [\x1b[96m") :-len("\x1b[0m]\n")]
    assert out == "####"

def test_progress_bar_error(capsys):
    progress_bar(8, 10, "#", 10)
    out, err = capsys.readouterr()
    out = out[len("\x1b[93m(1/10)\x1b[0m  10.00% [\x1b[96m") :-len("\x1b[0m]\n")]
    assert out != "#####"