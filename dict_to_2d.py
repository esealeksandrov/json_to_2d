"""
    functions for prepare dicts
"""


def join_path(root: str, path: str, delimiter: str = "."):
    return delimiter.join(filter(None, (root, path)))


def dict_to_2d_dict(arr: (dict, list), root: str = None):
    if not isinstance(arr, (dict, list)):
        raise ValueError("Not dict or list")
    result = {}
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
                join_path(root, key): value for key, value in dict_to_2d_dict(value, key).items()
            })
    return result


def dict_to_2d_list(arr: (dict, list), path: list = None):
    """ Create list[tuple] from dict.
        tuple[0] - json path,
        tuple[1]- value
        arr - dict or list
        root - list of steps in json path from root
    """
    if not isinstance(arr, (dict, list)):
        raise ValueError(f"first param must be list or dict. Not \"{type(arr)}\"")
    result = []
    if isinstance(arr, dict):
        for key, value in arr.items():
            if isinstance(value, (dict, list)):
                result += dict_to_2d_list(value, path + [key] if path is not None else [key])
            else:
                result.append((".".join(path + [key] if path is not None else [key]), value))
    else:
        for value in arr:
            key = "#"
            if isinstance(value, (dict, list)):
                result += dict_to_2d_list(value, path + [key] if path is not None else [key])
            else:
                result.append((".".join(path + [key] if path is not None else [key]), value))
    return result