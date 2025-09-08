import datetime

def log_request(client_ip, method, path, status_code):
    timestamp = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
    log_entry = f'{client_ip} - - [{timestamp}] "{method} {path} HTTP/1.1" {status_code} -\n'

    try:
        with open('logs/access.log', 'a') as f:
            f.write(log_entry)
    except:
        pass
