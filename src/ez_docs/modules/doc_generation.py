import re
import unicodedata
import os


def loc_sub(text, key, value):
    # Find the keys using sub-strings.
    pattern = f"<<{key}>>"
    # Replace occurrences of a particular sub-string with another.
    text = re.sub(pattern, value, text)
    return text


def slugify(value, allow_unicode=False):
    # Taken from https://github.com/django/django/blob/master/django/utils/text.py
    """
    # Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    # dashes to single dashes. Remove characters that aren't alphanumerics,
    # underscores, or hyphens. Convert to lowercase. Also strip leading and
    # trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def recognize_file_name(key_value: str, file_name_key: str):
    # Search for the keys, then replace the pattern with the indicated key.
    final_name = file_name_key
    for key in key_value.keys():
        pattern = rf'{key}(?=[:\-_ .,\s]|$)'
        final_name = re.sub(pattern, key_value[key], final_name)
    return slugify(final_name)


def doc_generator(directory_template: str, key_value: dict, file_name_key: str, flag: int = 1):
    # Open the indicated directory.
    with open(directory_template, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        input_file.close()
    filename = recognize_file_name(key_value, file_name_key)
    # Generates the file replacing data by data
    with open(f"./output/{filename}.md", "w+", encoding="utf-8") as input_file:
        for key in key_value.keys():
            text = loc_sub(text, key, key_value[key])
        input_file.write(text)
    if flag == '1':
        os.system(f"mdpdf -o ./output/{filename}.pdf ./output/{filename}.md")
