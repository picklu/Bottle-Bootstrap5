from os import path
from glob import glob
import json


def combine_json_files(files):
    """Combine json files into a single json file"""

    data = []
    for file in files:
        with open(file, mode="r", encoding="utf8") as f:
            ed = json.loads(f.read())
            old_data = list(ed.values())
            for edata in old_data:
                for article in edata:
                    data.append(article)
    return data


def combine_json_files_with_keys(files):
    """Combine json files into a single json file"""

    data = []
    for file in files:
        with open(file, mode="r", encoding="utf8") as f:
            dataset = json.loads(f.read())
            for key in dataset:
                for article in dataset[key]:
                    article["key"] = key[:50]
                    data.append(article)
    return data


def get_data(fileName):
    """Return data in json format"""
    data = []
    with open(fileName, mode="r", encoding="utf8") as f:
        data = json.loads(f.read())

    return data


if __name__ == "__main__":
    current_path = path.dirname(__file__)
    data_folder = "data"
    file_name_pattern = "*.json"
    files = glob(path.join(current_path, data_folder, file_name_pattern))
    data = combine_json_files_with_keys(files)
    with open("combined_data.json", "w") as f:
        json.dump(data, f)
