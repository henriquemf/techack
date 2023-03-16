from nmap import nmap

nm = nmap.PortScanner()

def scan_port(ip, port):
    nm.scan(ip, port)
    return nm[ip]['tcp'][int(port)]['state']

if __name__ == '__main__':
    print("-"*30 + "\n" + " BEM VINDO AO NMAP SCANNER \n" + "-"*30 + "\n")
    ip = input("Digite o IP: \n")
    port = input("Digite a porta: \n")
    print("O estado da porta é: " + scan_port(ip, port))

