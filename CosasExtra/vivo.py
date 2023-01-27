# Abro y leo linea a linea las ips de negativos.txt y hago un ping para ver si estan vivas

import os            

# Escribo en vivo.txt las ips de negativos.txt que estan vivas

with open('negativos.txt', 'r') as f:
    ips = f.readlines()


with open('vivo.txt', 'w') as f:
    
    for ip in ips:
        # hago un ping a la ip
        res = os.system('ping -n 1 ' + ip.strip())
        # si el ping devuelve 0, la ip esta viva
        if res == 0:
            f.write(ip.strip() + "\n")
            print(ip.strip() + " esta viva")