import os
import platform
# print("#"*60)
# ip_host = input("Digite o IP a ser verificado: ")
# print("-"*60)
# os.system('ping {}'.format(ip_host))

current_os = platform.system().lower()


parameter = "-c"

ip = "8.8.8.8"
print (os.system(f"ping {parameter} 1 -w2 {ip} > /dev/null 2>&1"))

