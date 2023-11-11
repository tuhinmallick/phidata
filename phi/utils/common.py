from typing import Any, List, Optional, Type


def isinstanceany(obj: Any, class_list: List[Type]) -> bool:
    """Returns True if obj is an instance of the classes in class_list"""
    return any(isinstance(obj, cls) for cls in class_list)


def str_to_int(inp: Optional[str]) -> Optional[int]:
    """
    Safely converts a string value to integer.
    Args:
        inp: input string

    Returns: input string as int if possible, None if not
    """
    if inp is None:
        return None

    try:
        return int(inp)
    except Exception:
        return None


def is_empty(val: Any) -> bool:
    """Returns True if val is None or empty"""
    return val is None or len(val) == 0 or val == ""


def get_image_str(repo: str, tag: str) -> str:
    return f"{repo}:{tag}"
