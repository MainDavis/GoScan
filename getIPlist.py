# Leo el primer parametro que es el nombre de la carpeta donde está ip_ranges.csv, lo leo y recogo los datos de la columna 'Rango', lo paso de CIDR a IP y lo guardo en un fichero llamado ip_list.txt

import sys
import csv
import ipaddress

# Leo el primer parametro que es el nombre de la carpeta donde está ip_ranges.csv
folder = sys.argv[1]

# Leo el fichero ip_ranges.csv
with open(folder + '/ip_ranges.csv', 'r') as f:

    # Leo los datos de la columna 'Rango'
    reader = csv.DictReader(f)
    ip_ranges = [row['Rango'] for row in reader]

# Paso de CIDR a IP
ip_list = []
for ip_range in ip_ranges:
    for ip in ipaddress.ip_network(ip_range):
        ip_list.append(str(ip))

# Guardo los datos en un fichero llamado ip_list.txt
with open(folder + '/ip_list.txt', 'w') as f:
    for ip in ip_list:
        f.write(ip + '\n')

# Path: getIPlist.py