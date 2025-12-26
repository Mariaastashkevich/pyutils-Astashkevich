import json
from typing import Any
import pathlib
from pyutils.errors import JsonLoadError


def load_json(path: pathlib.Path) -> list[dict[str, Any]]:
    """ Safely loads list-of-dicts from JSON file """
    try:
        text = path.read_text(encoding='utf-8')
        data = json.loads(text)
        return data
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as exc:
        match exc:
            case FileNotFoundError():
                raise JsonLoadError('File not found') from exc
            case PermissionError():
                raise JsonLoadError('Permission denied') from exc
            case json.JSONDecodeError():
                raise JsonLoadError('Invalid JSON') from exc
            case _:
                raise JsonLoadError('Unexpected error while reading JSON') from exc


def save_json(data, path:pathlib.Path) -> None:
    """ Saves list-of-dicts to JSON file """
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')