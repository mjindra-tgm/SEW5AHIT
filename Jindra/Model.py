import socket
import threading

from PySide.QtCore import Slot
from tkinter import messagebox


class Server(threading.Thread):
    """
    The Main Thread, to controll and accept connections
    """


    def __init__(self, form, port, signal):
        """
        Constructor
        :param form: Gui to edit fields
        :param port: Port to listen
        """
        threading.Thread.__init__(self)
        self.port = port
        self.form = form
        self.serverList=[]
        self.running = True
        self.signal = signal
        self.i = 0
        signal.stopSignal.connect(self.stop)
        signal.refreshSignal.connect(self.refresh)
        signal.stopCon.connect(self.stopConnection)
        signal.newmsg.connect(self.msg)

    def run(self):
        """
        Just the run(connecting to clients and opening sub-threads)
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.serversocket:
            self.serversocket.bind(("localhost", self.port))
            self.serversocket.listen(5)
            try:
                while self.running:
                    print("Auf client warten...")
                    connection, client_address = self.serversocket.accept()
                    s = ServerThread(self.i, connection, self.signal)
                    self.i += 1
                    s.start()
                    self.serverList.append(s)
                self.serversocket.close()

            except socket.error as serr:
                print("Socket closed.")

    def refresh(self):
        """
        Clear the Server List in the GUI and refill it
        """
        self.signal.clear()
        for server in self.serverList:
            self.signal.new_User(server.name)

    def stop(self):
        """
        Should stop the Thread
        """
        self.running=False

    @Slot(int)
    def stopConnection(self, i):
        """
        Deletes an element from the serverList
        """
        for server in self.serverList:
            if server.number > i:
                server.number -= 1
        self.serverList.pop(i)


    @Slot(str)
    def msg(self, txt):
        for server in self.serverList:
            server.connection.send(txt.encode())


class ServerThread(threading.Thread):
    """
    Connection to a Client
    """

    def __init__(self, number, connection, signal):
        """
        Constructor
        :param number: Number in List
        :param connection: Connection from the Main Server Thread
        """
        threading.Thread.__init__(self)
        self.connection = connection
        self.number = number
        self.signal = signal

    def run(self):
        """
        The run. Receives Messages and sends them throughout all other sockets
        """
        self.name = self.connection.recv(1024).decode()
        self.signal.new_User(self.name)
        while True:
            data = self.connection.recv(1024).decode()
            if not data:
                self.connection.close()
                break

            elif data == "exit":
                self.signal.stopConnection(self.number)
                self.signal.refresh()
                self.connection.send("Bye!".encode())
                self.connection.close()
                return

            self.signal.msg(data)
        print("end")


class Client(threading.Thread):
    """
    Connection to the Server
    """
    i = 1

    def __init__(self, signal, host, name, port):
        """
        Constructor
        :param form: GUI to edit
        :param host: Hostname, or IP- Address
        :param name: Username of the Client
        :param port: Port to connect
        """
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.signal = signal
        self.running = True
        self.name = name
        Client.i += 1

    def run(self):
        """
        Receives Messages
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.clientsocket:
            try:
                self.clientsocket.connect((self.host, self.port))
                self.clientsocket.send(self.name.encode())
                while self.running:
                    data = self.clientsocket.recv(1024).decode()
                    self.signal.msg(data)

                    if data == "Bye!":
                        self.clientsocket.close()
                        break

            except socket.error as serr:
                print("Socket error: " + serr.strerror)
                messagebox.showinfo("Error", serr.strerror)

    def send(self, text):
        """Send messages"""
        text = self.name + ": " + text
        self.clientsocket.send(text.encode())
        self.signal.clear()
