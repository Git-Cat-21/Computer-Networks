# Computer Networks
## Online Shopping System
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