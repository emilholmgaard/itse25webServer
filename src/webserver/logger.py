import datetime
import uuid
import uuid_utils as uuid

def log_request(client_ip, method, path, status_code):
    uuid.uuid7()
    timestamp = datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')
    log_entry = f'uuid: {uuid.uuid7()}\n'
    log_entry += f'client ip: {client_ip}\n'
    log_entry += f'timestamp: {timestamp}\n'
    log_entry += f'method: {method}\n'
    log_entry += f'path: {path}\n'
    log_entry += f'HTTP/1.1\n'
    log_entry += f'status code: {status_code}\n\n'

    try:
        with open('logs/access.log', 'a') as f:
            f.write(log_entry)
    except:
        pass
