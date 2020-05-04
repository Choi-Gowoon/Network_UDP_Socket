import time
import socket

# const data
COUNT = 10
DEST = ("127.0.0.1", 12000)
BUF_SIZE = 1024

# func : alert starting
def printStart():
    print("Start Socket Client Program !")
    print("-------------------------------")

# func : create socket
def createSocket():
    # Creat Socket and Set the Socket timeout
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(1)
    return clientSocket

# func : send message from client to server
def sendMessage(clientSocket):
    # init sequence number
    sequenceNumber = 1
    while sequenceNumber <= COUNT:
        # time when client send message setting using perf_counter for correct calculating rtt
        startTime = time.perf_counter()
        # input message
        text = input("Type message : ")
        # init message format
        message = f"Ping   sequence number:{sequenceNumber}   time:{startTime}   \"{text}\""
        # ip address binding and send encoding message
        clientSocket.sendto(message.encode(), DEST)
        # print message that client send
        print(f"Client : {message}")
        # receive response from server
        receiveResponse(startTime)
        # progress sequence number
        sequenceNumber += 1
    # close socket
    clientSocket.close()

# func : calculate RTT
def calculaeRTT(startTime):
    # using perf counter for correct calculating rtt
    rtt = time.perf_counter() - startTime
    return str(rtt)

# func : receive response from server
def receiveResponse(startTime):
    # receive reply with time out exception
    try:
        # reply from server
        message, address = clientSocket.recvfrom(BUF_SIZE)
        # calculate rtt
        rtt = calculaeRTT(startTime)
        # print response decoding message from server
        print(f"Response Message : Success !\nmessage : {message.decode()}\nRTT : {rtt}\n")
    # handle timeout exception
    except socket.timeout:
        # print time out message
        print("Request Timed Out ! \n")

# func : close socket
def closeSocket(clientSocket):
    socket.close(clientSocket)

# func : alert ending
def printEnd():
    print("-------------------------------")
    print("END !")

# main thread
printStart()
clientSocket = createSocket()
sendMessage(clientSocket)
printEnd()
