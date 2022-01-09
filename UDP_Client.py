import socket

target_host = "127.0.0.1"
target_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # bir soket nesnesi oluşturma
# Soket nesnesini oluştururken soket türünü SOCK_DGRAM olarak değiştiririz. 
# UDP bağlantı gerektirmeyen bir protokol olduğundan, connect() çağırısı yoktur. Direkt sendto() ile veri gönderilir.

client.sendto("FurkanEnesPolatoglu".encode(encoding='utf-8'), (target_host, target_port))  # bazı veriler gönder 

data, addr = client.recvfrom(4096) # Son adım, UDP verilerini geri almak için recvfrom() çağrısı yapmaktır. 

print(data)

# Ayrıca, hem verileri hem de uzak ana bilgisayarın ve bağlantı noktasının ayrıntılarını döndürdüğünü de fark edeceksiniz.

