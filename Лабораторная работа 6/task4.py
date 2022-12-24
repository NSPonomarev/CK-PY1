import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:  # TODO реализовать конвертер из csv в json
        dict_list = []
        lines = [line.strip(new_line).split(delimiter) for line in f]
        start = 0
        headers = lines[start]
        for rows in lines[start + 1:]:
            dict_list.append({})
            for index, value in enumerate(rows):
                dict_list[-1][headers[index]] = value
    return dict_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#
