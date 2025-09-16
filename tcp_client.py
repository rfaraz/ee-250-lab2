"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
     # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = "172.20.10.5" # designated IP
    PORT = 12345 # designated port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT)) # connect socket to server at designated IP and port

        # TODO: Get user input and send it to the server using your TCP socket
        message = input("Enter what you want to send over the TCP socket: ")
        s.sendall(message.encode("utf-8")) # send the message in bytes
    
        # TODO: Receive a response from the server and close the TCP connection
        data = s.recv(1024) # read a maximum of 1024 bytes
    print("Received:", repr(data))
    s.close()

if __name__ == '__main__':
    main()