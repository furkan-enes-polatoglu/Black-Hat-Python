import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # bir soket nesnesi oluşturma
# AF_INET parametresi, standart bir IPv4 adresi veya ana bilgisayar adı kullanacağımızı belirtir.
# SOCK_STREAM parametresi, bunun bir TCP istemcisi olacağını gösterir.

client.connect((target_host,target_port))  # istemciyi bağlama

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode(encoding='utf-8'))  # bazı veriler gönder 

response = client.recv(4096) # bazı veriler al

print(response)  # Son adım, bazı verileri geri almak ve yanıtı yazdırmaktır. 