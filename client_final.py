import socket
import ssl
import pickle
SERVER_HOST_SSL = 'localhost' 
SERVER_PORT_SSL = 5555
SERVER_HOST_UDP = 'localhost' 
SERVER_PORT_UDP = 5555
# Create a TCP socket
client_socket_ssl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Load SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Wrap the socket with SSL
ssl_socket = ssl_context.wrap_socket(client_socket_ssl, server_hostname=SERVER_HOST_SSL)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
# Connect to the server via SSL
ssl_socket.connect((SERVER_HOST_SSL, SERVER_PORT_SSL))

# Receive a message from the server over SSL
data = ssl_socket.recv(1024)
print("Received from server (SSL):", data.decode())

# Close the SSL connection
ssl_socket.close()

# UDP Client
client_socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name=input("Enter the username ")
passw=input("Enter the pasword ")
if(name=="root" and passw=="root"):
    check = True
elif (name=="root1" and passw=="root1"):
    check=True
else:
    check=False

while check:
    print("1. Browse  2. Purchase  3. Print Receipt  4. Exit\n")
    ch = input("Choose from above\n")
    message = ch
    if ch == "1":
        print("BROWSING ITEMS\n")
        print("1. Electronics\n2. Cosmetics\n3. Clothes\n4. Shoes\n5. House-hold items")
        ch1 = input("Enter the category: ")
        message1 = ch1
        client_socket_udp.sendto(message.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))  # options
        client_socket_udp.sendto(message1.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))  # subcategory
        print("Sno   Item-Name   Quantity   Price\n")
        for _ in range(5):
            modified_message, server_address = client_socket_udp.recvfrom(2048)
            print(pickle.loads(modified_message))
        print("\n")

    elif ch == "2":
        print("PURCHASE ITEMS\n")
        ch1 = input("Enter the Serial Number of the item you wish to purchase: ")
        message1 = ch1
        ch2 = input("Enter the Quantity of the item: ")
        message2 = ch2
        if int(ch2) <= 0:
            print("Invalid Entry\n")
        else:
            client_socket_udp.sendto(message.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))
            client_socket_udp.sendto(message1.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))  # serial number
            client_socket_udp.sendto(message2.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))  # quantity
            modified_message, server_address = client_socket_udp.recvfrom(4096)
            
            print("item added to the cart")
        print("\n")
    elif ch == "3":
        s=0
        print("PRINT RECEIPT\n")
        client_socket_udp.sendto(message.encode("utf-8"), (SERVER_HOST_UDP, SERVER_PORT_UDP))
        modified_message1, _ = client_socket_udp.recvfrom(4096)
        modified_message2, _ = client_socket_udp.recvfrom(4096)
        print("Final Receipt\n")
        print("\n")
        total_cost = 0  
        print("Final Receipt\n")
        for item in (pickle.loads(modified_message1)):
            print(item)  
            item_cost = int(item[2]) * int(item[3])
            total_cost += item_cost
        print("Total Cost:", total_cost)
    elif ch=="4":
        print("Thank you exit......")
        break
    else:
        print("Wrong choice....")
client_socket_udp.close()