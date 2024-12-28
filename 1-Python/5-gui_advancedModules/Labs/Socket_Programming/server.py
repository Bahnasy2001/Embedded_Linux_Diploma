import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPv4,TCP
ip=socket.gethostbyname(socket.gethostname())
print("your ip is : "+ip)
print("=" * 20)
s.bind((ip,5000))
s.listen(5)
while True:
    client,address = s.accept()#waiting
    rodata=client.recv(1024)
    print(f"{address} is sending  to you this message {rodata.decode('UTF-8')}")
    print("=" * 20)
    msg=str(input("please enter the message that you want to send: "))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    client.close() 