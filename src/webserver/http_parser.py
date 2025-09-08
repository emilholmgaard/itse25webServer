def parse_request(request):
    try:
        lines = request.split('\r\n')
        request_line = lines[0]
        parts = request_line.split()

        if len(parts) < 3:
            raise ValueError("Invalid request line")

        method = parts[0]
        path = parts[1]
        version = parts[2]

        return method, path, version

    except Exception as e:
        raise ValueError(f"Invalid HTTP request: {e}")


def is_valid_request(method, version):
    valid_methods = ['GET']
    valid_versions = ['HTTP/1.0', 'HTTP/1.1']

    return method in valid_methods and version in valid_versions
