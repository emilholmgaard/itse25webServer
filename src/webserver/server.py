import socket
from request_handler import handle_request

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"http://{host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            handle_request(conn, addr)
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()
