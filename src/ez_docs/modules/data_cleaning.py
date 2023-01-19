import pandas as pd
from usable import find_delimiter

def filter_data(location):
    start_data = []

    #Tries to open the file at location
    try:
        #Checks if extension is csv, xlsx or html
        extension = location.split(".")[-1]
        if extension == "csv": start_data = pd.read_csv(location, delimiter=find_delimiter(location))
        elif extension == "html": start_data = pd.read_html(location)
        elif extension == "json": start_data = pd.read_json(location)
        elif extension == "xlsx": start_data = pd.read_excel(location)
        elif extension == "xml": start_data = pd.read_xml(location)
        else: raise Exception(f"The extension '{extension}' is not accepted.\nValid: csv, html, json, xlsx, xml")

        # Delete duplicates and incomplete lines
        start_data.dropna(inplace=True)
        start_data.drop_duplicates(inplace=True)

        """
        Converts the data_set to the format specified in the architecture:
        key_value = [
            {
            "field 1": "value 1",
            "...": "...",
            "field n": "value n"
            },
        ]
        """
        final_data = []
        for line in range(len(start_data)):
            final_data.append({})
            for col in list(start_data.columns):
                final_data[line][col] = str(start_data.iloc[line][col])
        return final_data
    except FileNotFoundError:
        print("Error: The dataset file was not found.")
        return start_data