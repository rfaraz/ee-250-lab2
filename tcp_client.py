"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():

    HOST = "127.0.0.1"    # The remote host
    PORT = 12345              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT)) # connect socket to server at designated IP and port
        message = input("Enter what you want to send over the TCP socket: ") # get user input to send
        s.sendall(message.encode("utf-8")) # send the message in bytes
        data = s.recv(1024) # read a maximum of 1024 bytes
    print("Received:", repr(data))
    s.close()

    # TODO: Create a socket and connect it to the server at the designated IP and port


    # TODO: Get user input and send it to the server using your TCP socket


    # TODO: Receive a response from the server and close the TCP connection




if __name__ == '__main__':
    main()