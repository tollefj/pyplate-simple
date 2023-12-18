import json
import os
from typing import Any, List


def read_file(file_path: str, encoding: str = "utf-8") -> str:
    with open(file_path, "r", encoding=encoding) as file:
        return file.read()


def write_file(file_path: str, content: str, encoding: str = "utf-8") -> None:
    with open(file_path, "w", encoding=encoding) as file:
        file.write(content)


def read_json(file_path: str) -> Any:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(file_path: str, data: Any) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def create_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def list_files(directory_path: str) -> List[str]:
    return os.listdir(directory_path)
