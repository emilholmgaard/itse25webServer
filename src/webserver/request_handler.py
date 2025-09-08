from http_parser import parse_request, is_valid_request
from file_handler import get_file_path, is_safe_path, read_file, get_content_type
from response_builder import create_success_response, create_error_response
from logger import log_request

def handle_request(connection_socket, addr):
    try:
        request = connection_socket.recv(1024).decode('utf-8')
        if not request:
            return

        method, path, version = parse_request(request)

        if not is_valid_request(method, version):
            response = create_error_response(400, "Bad Request")
            connection_socket.send(response.encode('utf-8'))
            log_request(addr[0], method, path, 400)
            return

        filename = get_file_path(path)

        if not is_safe_path(filename):
            response = create_error_response(400, "Bad Request")
            connection_socket.send(response.encode('utf-8'))
            log_request(addr[0], method, path, 400)
            return

        try:
            content = read_file(filename)
            content_type = get_content_type(filename)
            response = create_success_response(content, content_type)
            connection_socket.send(response.encode('utf-8'))
            log_request(addr[0], method, path, 200)

        except FileNotFoundError:
            response = create_error_response(404, "Not Found")
            connection_socket.send(response.encode('utf-8'))
            log_request(addr[0], method, path, 404)

        except Exception:
            response = create_error_response(500, "Internal Server Error")
            connection_socket.send(response.encode('utf-8'))
            log_request(addr[0], method, path, 500)

    except ValueError:
        response = create_error_response(400, "Bad Request")
        connection_socket.send(response.encode('utf-8'))
        log_request(addr[0], "GET", "/", 400)

    except Exception:
        response = create_error_response(500, "Internal Server Error")
        connection_socket.send(response.encode('utf-8'))
        log_request(addr[0], "GET", "/", 500)

    finally:
        connection_socket.close()
