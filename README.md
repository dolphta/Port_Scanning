#module_socket.py reads ips from ip.txt file and scans ports between 1 and 25 by using socket module. If it finds any open port, adds the port number to port_list and also receive the banner from that port and add it to banner list. Finally, prints all open ports and and banners.

#module_socket_2.py is specialized version of module_socket. It has and addition code piece that checks if banners has string "SSH" it makes a guess on target system and prints "System might be Linux or a network device!". After that, it creates a log.txt file and logs the ip adresses into that file
