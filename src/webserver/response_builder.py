from file_handler import read_file

def create_success_response(content, content_type):
    return (
        f"HTTP/1.1 200 OK\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(content)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{content}"
    )


def create_error_response(status_code, message):
    error_files = {
        400: 'html/400.html',
        404: 'html/404.html',
        500: 'html/500.html'
    }

    try:
        html = read_file(error_files.get(status_code, 'html/404.html'))
    except:
        html = f"<html><body><h1>{status_code} {message}</h1></body></html>"

    return (
        f"HTTP/1.1 {status_code} {message}\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(html)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{html}"
    )
