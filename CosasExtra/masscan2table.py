# Leo el json de masscan y lo guardo en un archivo llamado servicios.csv

import json
import os

puertos_servicios = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternativo",
    179: "BGP",
    443 : "HTTPS",
    8443: "HTTPS Alternativo",
    447: "IEC 60870-5-104",
    3478: "STUN",
    5060: "SIP",
    5222 : "XMPP",
    5061 : "SIP over TCP/TLS",
    8008 : "HTTP Alternativo",
    1720 : "H.323"
}


# Leo el json de masscan y lo guardo en un archivo llamado servicios.csv
with open('output.json', 'r') as f:
    data = json.load(f)

with open('servicios.csv', 'w') as f:
    f.write("ip;port;Posible servicio;ttl\n")
    for host in data:
        ip = host["ip"]

        puertos = ""
        
        for port in host["ports"]:
            puertos = puertos + "," + str(port["port"])
            # Si el puerto esta en el diccionario de puertos_servicios, pongo la variable servicio con el nombre del servicio y si no, pongo ???
            if port["port"] in puertos_servicios:
                servicio = puertos_servicios[port["port"]]
            else:
                servicio = "???"

        ttl = port["ttl"]
        
        


        f.write(f"{ip};{puertos};{servicio};{ttl}\n")
