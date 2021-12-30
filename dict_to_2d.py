import json
from collections import defaultdict

from data import simple_mess, strange_mess


def join_path(root: str, path: str, delimiter: str = "."):
    return delimiter.join(filter(None, (root, path)))


def dict_to_two_d(arr: (dict, list), root: str = None):
    result = {}
    if isinstance(arr, (dict, list)):
        path_prefix = "#" if isinstance(arr, list) else None
        for item_key in (
                arr if isinstance(arr, dict)
                else range(len(arr))
        ):
            key = join_path(path_prefix, str(item_key), "")
            value = arr[item_key]
            if isinstance(value, (int, str, bool, float)):
                result[join_path(root, key)] = value
            elif isinstance(value, (dict, list)):
                result.update({
                    join_path(root, key): value for key, value in dict_to_two_d(value, key).items()
                })
    return result




if __name__ == "__main__":
    from datetime import datetime as d
    from pympler import asizeof
    from data import test_data

    loop = 100000

    s = d.now()
    for i in range(loop):
        dict_to_two_d(json.loads(test_data))
    print(loop, " = ", d.now() - s)
    #
    # print("dict: ",asizeof.asizeof(d)/8 ," list(tuple) ", asizeof.asizeof(t)/8)
    # print(d)