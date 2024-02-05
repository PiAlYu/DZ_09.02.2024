from ipaddress import *

for i in range(32, -1, -1):
    network1 = ip_network(f'201.92.0.20/{i}', 0)
    network2 = ip_network(f'201.92.0.49/{i}', 0)
    if network1 == network2:
        print(2 ** (32 - i) - 4)
        break
