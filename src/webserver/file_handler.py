import os


def get_content_type(filename):
    return "text/html"


def get_file_path(request_path: str) -> str:
    if request_path == "/":
        return "html/index.html"
    return "html/" + request_path.lstrip("/")


def is_safe_path(path: str, base: str = "html") -> bool:
    full_path = os.path.abspath(os.path.join(base, path.lstrip("/\\")))
    base_path = os.path.abspath(base)
    return full_path.startswith(base_path)


def read_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
