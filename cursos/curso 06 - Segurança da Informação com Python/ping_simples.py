import os

print("#"*60)
ip_host = input("Digite o IP a ser verificado: ")
print("-"*60)
os.system('ping {}'.format(ip_host))
