import socket
import subprocess
from tqdm import tqdm
import os
import time
import pyfiglet
from termcolor import colored

# --------------------------------------------------------------------------------
#                                      FUNÇÕES
# --------------------------------------------------------------------------------

def inicio():
    texto = "\n PORT SCANNER"
    titulo = pyfiglet.figlet_format(texto, font="slant")

    colored_ascii_banner = colored(titulo, 'green')
    print(colored_ascii_banner)
    print("\033[1;32m-\033[00m"*50)
    print(" "*12 + "\033[1;32mBEM VINDO AO PORT SCANNER\033[00m" + " "*12)
    print("\033[1;32m-\033[00m"*50 + "\n")

    time.sleep(1)
    print("Carregando mapa de rede...\n")
    time.sleep(1)

    #get_ip()

    ip = input("Digite o IP desejado: \n")

    if ip == "":
        print("\033[31mDigite um IP válido\033[00m\n")
        inicio()

    ports_input = input("Digite o RANGE de portas separado por uma vírgula | Digite uma única porta | ENTER para mapear todas: \n")

    if ports_input == "":
        ports = list(range(1, 65536))
    elif "," in ports_input:
        start, end = map(int, ports_input.split(","))
        ports = list(range(start, end + 1))
    else:
        ports = [int(ports_input)]

    ports_map(ports, ip)

def get_ip():
    os.system("clear")

    print("\033[1;32m-\033[00m"*50)
    print(" "*12 + "\033[1;32mBEM VINDO AO PORT SCANNER\033[00m" + " "*12)
    print("\033[1;32m-\033[00m"*50 + "\n")

    time.sleep(1)

    print("\033[95m-\033[00m"*30)
    print(" "*6 + "\033[95mMAPEAMENTO DA REDE\033[00m" + " "*6)
    print("\033[95m-\033[00m"*30 + "\n")

    time.sleep(1)

    fix_ip = input("Digite os 3 primeiros números do endereço IP da rede (ex: 192.168.3): \n")	

    ips = [fix_ip + '.' + str(i) for i in range(1, 255)]

    available_ips = []

    for ip in tqdm(ips, desc="Verificando IPs"):
        response = subprocess.run(['ping', '-c', '1', '-w', '1', ip], stdout=subprocess.DEVNULL)
        if response.returncode == 0:
            available_ips.append(ip)

    print("IPs disponíveis: " + str(len(available_ips)) + "\n")

    for ip in available_ips:
        print(ip + " está disponível")

def ports_map(ports, ip):
    well_known_ports = {
        20: 'FTP (File Transfer Protocol)',
        21: 'FTP (File Transfer Protocol)',
        22: 'SSH (Secure Shell)',
        23: 'Telnet',
        25: 'SMTP (Simple Mail Transfer Protocol)',
        53: 'DNS (Domain Name System)',
        80: 'HTTP (Hypertext Transfer Protocol)',
        110: 'POP3 (Post Office Protocol version 3)',
        119: 'NNTP (Network News Transfer Protocol)',
        123: 'NTP (Network Time Protocol)',
        143: 'IMAP (Internet Message Access Protocol)',
        161: 'SNMP (Simple Network Management Protocol)',
        194: 'IRC (Internet Relay Chat)',
        443: 'HTTPS (HTTP Secure)',
        445: 'SMB (Server Message Block)',
        465: 'SMTPS (Simple Mail Transfer Protocol Secure)',
        514: 'Syslog',
        587: 'SMTP (Mail Submission)',
        631: 'IPP (Internet Printing Protocol)',
        873: 'rsync',
        993: 'IMAPS (Internet Message Access Protocol Secure)',
        995: 'POP3S (Post Office Protocol version 3 Secure)',
        1080: 'SOCKS (SOCKetS)',
        1194: 'OpenVPN',
        1433: 'Microsoft SQL Server',
        1434: 'Microsoft SQL Server',
        1521: 'Oracle',
        1723: 'PPTP (Point-to-Point Tunneling Protocol)',
        3306: 'MySQL',
        3389: 'RDP (Remote Desktop Protocol)',
        5432: 'PostgreSQL',
        5900: 'VNC (Virtual Network Computing)',
        5901: 'VNC (Virtual Network Computing)',
        5902: 'VNC (Virtual Network Computing)',
        5903: 'VNC (Virtual Network Computing)',
        6379: 'Redis',
        8080: 'HTTP Alternate (http_alt)',
        8443: 'HTTPS Alternate (https_alt)',
        9000: 'Jenkins',
        9090: 'HTTP Alternate (http_alt)',
        9091: 'HTTP Alternate (http_alt)'
    }
    
    open_ports = False
    for port in tqdm(ports, leave=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((ip, port))
            if result == 0:
                service_name = socket.getservbyport(port)
                well_known_service = well_known_ports.get(port)
                if port in well_known_ports.keys():
                    tqdm.write(f"Porta \033[35m{port}\033[00m (\033[33m{service_name}\033[00m) \033[32mSERVIÇO QUE DEVERIA RODAR: {well_known_service}\033[00m - {ip}")
                else:
                    tqdm.write(f"Porta \033[35m{port}\033[00m (\033[33m{service_name}\033[00m) \033[031mSERVIÇO DESCONHECIDO\033[00m - {ip}")
                open_ports = True
            s.close()

        except:
            continue

    print("\033[1;32mMapeamento completo!033[00m \n")

    if not open_ports:
        print("\033[31mNenhuma porta aberta encontrada\033[00m")


if __name__ == "__main__":
    inicio()