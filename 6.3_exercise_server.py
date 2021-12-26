import socket
import json
import math
import sys
import errno
import time
from multiprocessing import Process

def add(value1):
        x = int(value1[1])
        y = int(value1[2])
        print("Calculating addition process...")
        try:
                answer = x + y
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def subtract(value1):
        x = int(value1[1])
        y = int(value1[2])
        print("Calculating subtraction process...")
        try:
                answer = x - y
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def multiply(value1):
        x = int(value1[1])
        y = int(value1[2])
        print("Calculating multiplication process...")
        try:
                answer = int(x) * int(y)
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def division(value1):
        x = int(value1[1])
        y = int(value1[2])
        print("Calculating division process...")
        try:
                answer = x / y
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def log(value1):
        x = int(value1[1])
        print("Calculating log process...")
        try:
                answer = math.log(x,10)
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def sqrt(value1):
        x = int(value1[1])
        print("Calculating square root process...")
        if(x >= 0):
                try:
                        answer = math.sqrt(x)
                except:
                        answer = "Process cannot be calculated. Please try again..."
        else:
                answer = "Process cannot be calculated. Server cannot calculate negative value..."

        return answer

def exp(value1):
        x = float(value1[1])
        print("Calculating exponential process...")
        try:
                answer = math.exp(x)
        except:
                answer = "Process cannot be calculated. Please try again..."

        return answer

def process_start(s_sock):
        intro = "Client is connected to the server..."
        s_sock.sendall(str.encode(intro))
        while True:
                option = s_sock.recv(2048)
                option.decode('utf-8')
                if option:
                        option = json.loads(option)
                        print(option)
                        if(option[0] == 'add'):
                                answer = add(option)
                        elif(option[0] == 'subtract'):
                                answer = subtract(option)
                        elif(option[0] == 'multiply'):
                                answer = multiply(option)
                        elif(option[0] == 'division'):
                                answer = division(option)
                        elif(option[0] == 'sqrt'):
                                answer = sqrt(option)
                        elif(option[0] == 'log'):
                                answer = log(option)
                        elif(option[0] == 'exp'):
                                answer = exp(option)

                        message = "The answer is %s." % str(answer)
                        print("---------------------")
                        print("| Process Completed |")
                        print("---------------------\n")
                        s_sock.sendall(str.encode(message))
        s_sock.close()
        
if __name__ == '__main__':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 8888))
        print("\nWelcome to the server...")
        print("Server is listening for input from clients...\n")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock, s_addr = s.accept()
                                p = Process(target = process_start, args = (s_sock,))
                                p.start()

                        except socket.error:
                                print('Socket error problem occured!')

        except Exception as e:
                print('Exception problem occured!')
                print(e)
                sys.exit(1)

        finally:
                s.close()
