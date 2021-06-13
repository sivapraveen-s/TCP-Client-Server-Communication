import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1028))
com_info=''
while True: 
    msg=s.recv(7)
    if len(msg)<=0:
        break
    com_info += msg.decode("utf-8")
print(com_info)
