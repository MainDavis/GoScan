# Leo ip_list.txt y lo guardo en una lista

import os

# Leo el archivo ip_list.txt y lo guardo en una lista
with open('ip_list.txt', 'r') as f:
    ip_list = f.readlines()

# Leo el archivo sub.txt y lo guardo en una lista
with open('sub.txt', 'r') as f:
    sub = f.readlines()

# Escribo en positivos.txt las ips de ip_list.txt que estan en sub.txt
with open('positivos.txt', 'w') as f:
    for ip in ip_list:
        for linea in sub:
            subdomain, ip_s = linea.split(' ')
            # quito los corchetes de la ip
            ip_s = ip_s[1:-2]

            if ip.strip() == ip_s.strip():
                f.write(ip_s + ";" + subdomain + "\n")

# Escribo en negativos.txt las ips de ip_list.txt que no estan en sub.txt
with open('negativos.txt', 'w') as f:
    for ip in ip_list:
        for linea in sub:
            subdomain, ip_s = linea.split(' ')
            # quito los corchetes de la ip
            ip_s = ip_s[1:-2]

            if ip.strip() == ip_s.strip():
                break
        else:
            f.write(ip)

# Ahora negativos_lista.txt es una lista de ips de sub.txt que no estan en ip_list.txt
with open('negativos_lista.txt', 'w') as f:
    for linea in sub:
        subdomain, ip_s = linea.split(' ')
        # quito los corchetes de la ip
        ip_s = ip_s[1:-2]

        for ip in ip_list:
            if ip.strip() == ip_s.strip():
                break
        else:
            f.write(ip_s + "\n")