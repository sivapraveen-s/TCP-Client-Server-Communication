import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1028))
s.listen(5)
while True:
    clt,  adr=s.accept()
    print(f"Connection to {adr} established... ")
    clt.send(bytes("socket programming in pyhton","utf-8"))
    clt.close()