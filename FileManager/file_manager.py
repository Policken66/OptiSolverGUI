import json
import os
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
