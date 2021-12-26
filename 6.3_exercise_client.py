import socket
import json

ClientSocket = socket.socket()
host = '192.168.66.5'
port = 8888

def send(option,value1):
        test = [option,value1]
        test = json.dumps(test)
        ClientSocket.sendall(bytes(test,encoding = "utf-8"))

def send1(option,value1,value2):
        test = [option,value1,value2]
        test = json.dumps(test)
        ClientSocket.sendall(bytes(test,encoding="utf-8"))

print('\nWaiting for connection...')
print('Please wait while client connecting to server...')
try:
        ClientSocket.connect((host, port))
except socket.error as e:
        print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while True:

        state = 0
        while(state == 0):
                print('\nList of operation - [add][subtract][multiply][division][sqrt][log][exp]')
                option = input('Enter types of operation : ')
                if(option == 'add'):
                        value1 = input("Enter the First Value: ")
                        value2 = input("Enter the Second Value: ")
                        state = 1
                        send1(option,value1,value2)
                elif(option == 'subtract'):
                        value1 = input("Enter the First Value: ")
                        value2 = input("Enter the Second Value: ")
                        state = 1
                        send1(option,value1,value2)
                elif(option == 'multiply'):
                        value1 = input("Enter the First Value: ")
                        value2 = input("Enter the Second Value: ")
                        state = 1
                        send1(option,value1,value2)
                elif(option == 'division'):
                        value1 = input("Enter the First Value: ")
                        value2 = input("Enter the Second Value: ")
                        state = 1
                        send1(option,value1,value2)
                elif(option == 'sqrt'):
                        value1 = input("Enter the Value: ")
                        state = 1
                        send(option,value1)
                elif(option == 'log'):
                        value1 = input("Enter the Value: ")
                        state = 1
                        send(option,value1)
                elif(option == 'exp'):
                        value1 = input("Enter the Value: ")
                        state = 1
                        send(option,value1)
                else:
                        print("Operation not found. Please enter valid operation...")
                        state = 0

        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

ClientSocket.close()
