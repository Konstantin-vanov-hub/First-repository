import socket
from concurrent.futures import ThreadPoolExecutor

def get_service_name(port, protocol):
    try:
        return socket.getservbyport(port, protocol)
    except:
         return 'Unknown'

def scan_tcp_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            service = get_service_name(port, 'tcp')
            return f'TCP {port} ({service})'
    return None
   
def scan_ports(host, ports, max_workers = 100):
    open_ports = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        tcp_results = executor.map(lambda p: scan_tcp_port(host, p), ports)
    
        for result in tcp_results:
            if result:
                open_ports.append(result)
    return open_ports


def local_ip():
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    return ip_adress

ports_to_scan = range(1,1000)

ip_scan = input('Select IP: ')
if ip_scan == '0':
    target_ip = local_ip()

if ip_scan == '1':
    target_ip = input('IP:')

print(f'Scan: {target_ip}')
open_ports = scan_ports(target_ip, ports_to_scan)
if open_ports:
    print('Open ports: ')
    for port in open_ports:
        print(f'- Port {port}')
else:
    print('No open ports')

