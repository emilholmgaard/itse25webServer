from server import start_server
import netifaces

addr = netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']

HOST = addr
PORT = 9000

if __name__ == "__main__":
    start_server(HOST, PORT)
