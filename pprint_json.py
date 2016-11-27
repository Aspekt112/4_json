# -*- coding: utf-8 -*-

import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    description = 'Реализует функцию pretty_print для файлов JSON: ' \
                  'в качестве входного параметра следует передать путь до файла JSON, ' \
                  'содержимое которого будет выведено в консоль в удобном для чтения виде'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', '--filepath',
                        type=str,
                        required=True,
                        help='Путь до JSON файла.')

    args = parser.parse_args()

    json_content = load_data(args.filepath)
    if json_content is None:
        print('Файл пуст или не существует.')
    else:
        pretty_print_json(json_content)
