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
    description = 'Реализует функцию pretty_print для JSON: ' \
                  'на входе JSON файл, на выходе его содержимое в удобоном формате'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', '--filepath',
                        type=str,
                        required=True,
                        help='Путь до файла.')

    args = parser.parse_args()

    json_content = load_data(args.filepath)
    if json_content is None:
        print('Файл пуст или не существует.')
    else:
        pretty_print_json(json_content)
