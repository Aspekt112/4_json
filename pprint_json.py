# -*- coding: utf-8 -*-

import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        path = str(input('Введите путь к JSON файлу: '))
    except ValueError or TypeError:
        path = None
    if path is None:
        print('Некорректные данные. См. пример использования.')
    else:
        json_content = load_data(path)
        pretty_print_json(json_content)
