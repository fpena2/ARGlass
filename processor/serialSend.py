from bluetooth import *
import VideoProcessor

def connect():
    socket = BluetoothSocket(RFCOMM) # starts a bluetooth socket
    # connects to our RN-42 on port number 1
    socket.connect(("00:06:66:6B:B6:7A", 1))

    print("connected...")
    # call function to process video and send data to module
    VideoProcessor.getScreenData(socket)
    socket.close()

if __name__ == '__main__':
    connect()
