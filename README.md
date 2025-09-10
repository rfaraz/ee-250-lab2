# Lab 2: TCP, UDP, Socket Programming
## Leyaa George (7466104518), Rida Faraz (3638181021)

***Evaluating TCP vs UDP***

**Question 1**
The UDP was far less reliable when the 50% loss was added because some of the messages were not received at all. Around 50% or more messages were lost entirely. This most likely occurred because UDP sends the data before a connection is established, so some data is lost in the transfer process. 
It does not retransmit lost data in the case of package loss, as it has no protocol to detect it. 

**Question 2**
When we used TCP, it was far more reliable than UDP, as all messages were eventually loaded in. However, there was a delay in transmitting data. The reason for this is because TCP checks for package loss and retransmits necessary data in the case that loss occurs. 

**Question 3**
The TCP response time did become slower, which is most likely occurring because it is retransmitting data when it detects a loss. These extra checks and protocols add to the latency. 

***TCP Client & Server***

Questions in tcp_server.c:

1. They're command line parameters. argc is the number of arguments in the command line and argv is an array of the entered commands.

***REWORD 2 

2. A UNIX file descriptor is a small integer that represents an open file or resource in UNIX and a UNIX file descriptor table maps the file descriptor to actual structs in the kernel that manage the resource.

3. A struct is a blueprint for a custom data type. It is basically a class except everything is inherently public unless otherwise specified. The structure of sockaddr_in 

4. The input parameters of socket() are an address family, the socket type, and the protocol. The address family defines which family of address the socket can communicate with. In the code this is AF_INET which is ____. The socket type defines 
