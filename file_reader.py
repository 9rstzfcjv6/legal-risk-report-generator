import os


def read_contract_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_text_files(folder_path):
    files = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            files.append(file_name)

    return files