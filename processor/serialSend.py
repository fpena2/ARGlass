from bluetooth import *
import VideoProcessor


def connect():
    socket = BluetoothSocket(RFCOMM)
    socket.connect(("00:06:66:6B:B6:7A", 1))

    print("connected...")
    VideoProcessor.getScreenData(socket)
    socket.close()

if __name__ == '__main__':
    connect()
