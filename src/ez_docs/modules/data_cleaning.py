import pandas as pd


#Finds out which non-alphanumeric character separates a given csv file
def find_delimiter(location: str) -> str:
    delimiters_dict = {}
    file = open(location).read()
    delimiters_list = list(set([char for char in file if not (char.isalpha() or char.isspace() or char.isdigit())]))
    for line in file.split("\n"):
        for delimiter in delimiters_list:
            if not delimiter in delimiters_dict.keys(): delimiters_dict[delimiter] = []
            delimiters_dict[delimiter].append(len(line.split(delimiter)))
    for delimiter in delimiters_dict.keys(): delimiters_dict[delimiter] = len(set(delimiters_dict[delimiter]))
    delimiters_dict = sorted(delimiters_dict.items(), key=lambda item: item[1])
    return delimiters_dict[0][0]

# Returns a pandas DataFrame according to an extension
def filter_format(location: str) -> pd.DataFrame:
    extension = location.split(".")[-1]
    if extension == "csv": return pd.read_csv(location, delimiter=find_delimiter(location))
    elif extension == "html": return pd.read_html(location)
    elif extension == "json": return pd.read_json(location)
    elif extension == "xlsx": return pd.read_excel(location)
    elif extension == "xml": return pd.read_xml(location)
    else: raise Exception(f"\033[0;31mThe extension '{extension}' is not accepted.\nValid: csv, html, json, xlsx, xml.\033[0m")

#Checks if a given line passes a specified condition
def passes_constraint(const: list, dataset: pd.DataFrame, line):
    if not const: return True
    else:
        if const[0] not in dataset.columns: raise Exception("")
        if (type(line[const[0]]) is int and const[1] not in [">", ">=", "<", "<=", "==", "!="]) or (type(line[const[0]]) is str and const[1] not in ["==", "!="]): raise Exception("")
        if (type(line[const[0]]) is int) and eval(f"{line[const[0]]} {const[1]} {const[2]}"): return True
        if type(line[const[0]]) is str:
            if("*" in const[2][0] and "*" in const[2][-1] and const[2].strip("*") in line[const[0]]): return True
            elif(eval(f"'{line[const[0]]}' {const[1]} '{const[2]}'")): return True
    return False

# Converts the data_set to the format specified in the architecture
def filter_data(location: str, constraint: list = None) -> list:
    try:
        start_data = filter_format(location)
        if True in start_data.isna().values: print("\033[0;33mWarning: Your dataset file has incomplete lines. These ones will be ignored.\033[0m")
        start_data.dropna(inplace=True)
        start_data.drop_duplicates(inplace=True)
        return [{col: str(start_data.iloc[line][col]) for col in start_data.columns} for line in range(len(start_data)) if passes_constraint(constraint, start_data, start_data.iloc[line])]
    except FileNotFoundError: raise Exception("\033[0;31mThe dataset file was not found.\nPlease, make sure you have typed a correct file name.\033[0m")