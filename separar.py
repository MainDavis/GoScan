# Leo subdomains.txt y hago un split por espacio, luego escribo en dos ficheros la ip y el otro el subdominio

with open('sub.txt', 'r') as f:
    subdomains = f.read().splitlines()

with open('ip_subdominios.txt', 'w') as f:
    for subdomain in subdomains:
        ip, subdomain = subdomain.split(' ')
        f.write(ip)

with open('subdomains_list.txt', 'w') as f:
        for subdomain in subdomains:
            ip, subdomain = subdomain.split(' ')
            f.write(subdomain + '\n')
