import os

def get_content_type(filename):
    return 'text/html'

def get_file_path(request_path):
    return 'html/index.html' if request_path == '/' else 'html/' + request_path.lstrip('/')

def is_safe_path(path):
    return '..' not in path and not path.startswith('/')

def read_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
