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
    path = str(input('Введите путь к JSON файлу: '))
    json_content = load_data(path)
    if json_content is None:
        print('Файл пуст или не существует.')
    else:
        pretty_print_json(json_content)
