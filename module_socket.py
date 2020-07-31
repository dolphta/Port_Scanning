import socket

port_list = []
banner_list = []

file = open("ip.txt", "r")
ips = file.read()
file.close()

for ip in ips.splitlines():
    print(ip)

    for port in range(1,25):
        try:
            s = socket.socket()
            s.connect((str(ip), int(port)))
            banner = s.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            s.close()
            print(port)
            print(banner)
        except:
            pass

print(port_list)
print(banner_list)