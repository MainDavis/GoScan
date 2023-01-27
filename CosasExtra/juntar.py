# Leo ip_list.txt y sub.txt y los concateno en un archivo llamado ip_list_total.txt

import os

# Leo el archivo ip_list.txt y lo guardo en una lista
with open('ip_list.txt', 'r') as f:
    ip_list = f.readlines()
    for line in ip_list:
        line = line.strip()

# Leo el archivo sub.txt y lo guardo en una lista
with open('sub.txt', 'r') as f:
    sub = f.readlines()
    for line in sub:
        subdomain, ip = line.split(' ')
        # quito los corchetes de la ip
        ip = ip[1:-2]
        ip_list.append(ip.strip() + "\n")

# Escribo en ip_list_total.txt las ips de ip_list.txt y sub.txt
with open('ip_list_total.txt', 'w') as f:
    for ip in ip_list:
        f.write(ip)

# Ahora vuelvo a leer ip_list_total.txt y elimino las duplicadas
with open('ip_list_total.txt', 'r') as f:
    ip_list_total = f.readlines()
    ip_list_total = list(set(ip_list_total))

# Escribo en ip_list_total.txt las ips de ip_list.txt y sub.txt sin duplicados
with open('ip_list_total.txt', 'w') as f:
    for ip in ip_list_total:
        f.write(ip)