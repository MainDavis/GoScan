# Leo el archivo ip_subdominos.txt y borro las filas vacias

with open('ip_subdominios.txt', 'r') as f:
    ip_subdominos = f.read().splitlines()

with open('ip_subdominios.txt', 'w') as f:
    for ip_subdominio in ip_subdominos:
        if ip_subdominio != '':
            f.write(ip_subdominio + '\n')