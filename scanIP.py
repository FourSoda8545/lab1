# Escanner de direcciones IP dentro de una red.

import nmap

scanner = nmap.PortScanner()

ip = input("Inserte la IP a escannear: ")

print("Esta es la IP proporcionada: ", ip)
scanner.scan(ip)

print("Estas son las IP encontradas: ",scanner.all_hosts())