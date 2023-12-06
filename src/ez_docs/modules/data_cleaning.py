import pandas as pd


# Finds out which non-alphanumeric character separates a given csv file
def find_delimiter(location: str) -> str:
    delimiters_dict = {}
    file = open(location).read()
    temp_list = [
        char for char in file if not (
            char.isalpha() or char.isspace() or char.isdigit()
        )
    ]
    delimiters_list = list(set(temp_list))
    for line in file.split("\n"):
        for delimiter in delimiters_list:
            if delimiter not in delimiters_dict.keys():
                delimiters_dict[delimiter] = []
            delimiters_dict[delimiter].append(len(line.split(delimiter)))
    for delimiter in delimiters_dict.keys():
        delimiters_dict[delimiter] = len(set(delimiters_dict[delimiter]))
    delimiters_dict = sorted(delimiters_dict.items(), key=lambda item: item[1])
    return delimiters_dict[0][0]


# Converts the data_set to the format specified in the architecture
def filter_data(location: str, constraint: str = "") -> list:
    try:
        start_data = filter_format(location)
        if True in start_data.isna().values:
            print(
                    """
                    \033[0;33mWarning: Your dataset file has incomplete lines.
                    These ones will be ignored.\033[0m
                    """
                )
        start_data.dropna(inplace=True)
        start_data.drop_duplicates(inplace=True)
        if constraint:
            start_data.query(constraint[0], inplace=True)
        return [
            {
                col: str(start_data.iloc[line][col])
                for col in start_data.columns
            } for line in range(len(start_data))
        ]
    except FileNotFoundError:
        raise Exception(
            """
                \033[0;31mThe dataset file was not found.\n
                Please, make sure you have typed a correct file name.\033[0m
            """
        )

def filter_format(file_path):
    supported_extensions = {
        'csv': pd.read_csv,
        'xlm': pd.read_xml,
        'json': pd.read_json,
        'html': pd.read_html,
        'xlsx': pd.read_excel
    }
    
    extension = file_path.split('.')[-1]
    
    if extension in supported_extensions:
        return supported_extensions[extension](file_path)
    else:
        raise ValueError("The extension", '{extension}', "is not accepted.\n Valid: csv, html, json, xlsx, xml.")
