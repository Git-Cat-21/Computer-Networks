# Computer Networks
## Online Shopping System
### Step-By-Step Guide :
- Use ```git clone https://github.com/Git-Cat-21/Computer-Networks.git``` to make a copy of the project on your system
- Run the following command to start the server
- ```python server.py``` : This will **start both the TCP/SSL** and UDP servers. You should see messages indicating that the servers are listening for connections.
- Open Another Terminal/Command Prompt:
Run the following command to start the client ```python client.py```
- **Authenticate**:
Enter the username and password when prompted.
Valid credentials here are as follows:
 - Username: root, Password: root or 
 Username: root1, Password: root1
- Interact with the System and Enjoy !!!
- Follow this video to generate a self signed SSL certificate using OpenSSL : https://www.youtube.com/watch?v=c-LEHJy5g8Y
--------------------
- The ***online shopping system*** is a **network-based application** designed to facilitate secure and efficient e-commerce transactions. 
- Allowing **users to browse items, make purchases, and receive receipts through a combination of TCP/SSL and UDP protocols** which ensures secure communication. 
- It **provides a lightweight UDP-based mechanism for user interactions** such as browsing and purchasing items.

## Client_final.py
This Python script demonstrates a **client-side implementation** for a simple shopping application. It **includes SSL-secured communication** over **TCP and operations over UDP for handling user interactions**.

## Server_final.py
This code implements a server that **handles both TCP (with SSL) and UDP connections to facilitate a simple shopping application**. It  can send a test message over a secure TCP connection and **manage item browsing, purchasing, and receipt printing over UDP**.

## server.crt (Certificate)
- This is the **public certificate of the server**. It’s **issued** by a **Certificate Authority (CA)** and contains the **server’s public key** along with information about the server and the CA.

- It is **used to verify the identity of the server**. When a **client connects** to the server, the **server sends this certificate to the client to prove its identity**. The client can then use this certificate to **establish a secure connection**.

## server.csr (Certificate Signing Request)
- This is a **request file that you generate** and **send to a CA when you want to obtain a certificate (server.crt)**. It contains the public key and information about the organization and domain.
- The **CA uses the information** in this file **to create and sign your server certificate (server.crt)**. After verifying your details, the CA issues the certificate and sends it back to you.

## server.key (Private Key)
- This is the **private key associated with your server**. It’s **generated when you create the CSR** and is kept secret on the server. It should **never be shared or transmitted.**
- It’s **used to decrypt information sent to the server** and to **create digital signatures**. When a **client encrypts data using the public key** (from the certificate), the **server uses this private key to decrypt the data**. It’s also used to sign the CSR and to prove ownership of the certificate.