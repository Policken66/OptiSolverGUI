import json
import os
import re
from typing import Any, List, Tuple, Dict


def json_update(json_path: str, data: List[Tuple[str, Any]]) -> None:
    """
    Обновление данных в json файле.
    :param json_path: Путь до json файла.
    :param data: Формат [(Название переменной, значение), ...]
    :return:
    """
    # Загружаем существующие данные или создаем пустой словарь
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except (json.JSONDecodeError, Exception):
            existing_data = {}
    else:
        existing_data = {}

    # Обновляем данные
    for name, value in data:
        existing_data[name] = value

    # Сохраняем обновленные данные
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)


def data_from_json(json_path: str, names: List[str]) -> List[Any]:
    """
    Передается массив имен виджетов и путь до json файла.
    :param json_path: Путь до json файла.
    :param names: Имена виджетов.
    :return: Список значений в том же порядке, что и имена
    """
    if not os.path.exists(json_path):
        return [None] * len(names)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, Exception):
        return [None] * len(names)

    # Возвращаем значения для каждого имени, если имя не найдено - возвращаем None
    return [data.get(name) for name in names]


def dict_data_from_json(json_path: str, names: List[str]) -> Dict[str, Any]:
    """
    Передается массив имен виджетов и путь до json файла.
    :param json_path: Путь до json файла.
    :param names: Имена виджетов.
    :return: Словарь с ключами - именами виджетов и значениями из JSON
    """
    if not os.path.exists(json_path):
        return {name: None for name in names}

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, Exception):
        return {name: None for name in names}

    # Возвращаем словарь с ключами - именами виджетов
    return {name: data.get(name) for name in names}


def extract_parameters_from_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as file:
        parameters = json.load(file)
    return parameters


def change_params_in_template(template_path: str, data_dict: Dict[str, Any]) -> bool:
    lines = []
    with open(template_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []
    for l in lines:
        new_line = l
        for n in data_dict.keys():
            if str(n) + "=" in l:
                new_line = re.sub(f"{n}=[^\\s!]+", f"{n}={data_dict[n]}", l)
                break
        new_lines.append(new_line)

    with open(template_path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)

    return True


def get_all_text(template_path: str) -> str:
    lines = []
    with open(template_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return "".join(lines)
