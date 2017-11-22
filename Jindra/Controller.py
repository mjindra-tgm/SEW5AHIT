import sys

from PySide.QtCore import Signal
from PySide.QtCore import Slot
from PySide.QtGui import *
import ClientUI, ServerUI, Model
from Jindra import Start
from Jindra.Model import Server
from Jindra.SignalHandler import SignalHandler


class ClientController(QWidget):
    """
    MVC pattern: Creates a controller - mvc pattern - just for the client.
    """

    def __init__(self, host, name, port, parent=None):
        """
        Constructor
        :param host: Hostname or IP-Adress
        :param name: Client Name
        :param port: Port
        :param parent:
        """
        super().__init__(parent)
        self.running = True
        self.Form = ClientUI.ClientUI()
        self.Form.setupUi(self)
        self.connectButtons()
        self.signalHandler = SignalHandler()
        self.model = Model.Client(self.signalHandler, host, name, int(port))
        self.model.start()
        self.signalHandler.newmsg.connect(self.msg)
        self.signalHandler.stopSignal.connect(self.close)
        self.signalHandler.clearSignal.connect(self.clear)


    def connectButtons(self):
        """
        connects the button(s)
        """
        self.Form.send.clicked.connect(self.button)

    def button(self):
        """
        The Event Method called from the clicked button.
        """
        button = self.sender()
        if button == self.Form.send:
            self.model.send(self.Form.textEdit.toPlainText())

    def closeEvent(self, *args, **kwargs):
        """
        What to do, if the Window closes
        """
        if self.model:
            self.model.clientsocket.send("exit".encode())

    @Slot(str)
    def msg(self, txt):
        self.Form.textBrowser.append(txt)

    def clear(self):
        self.Form.textEdit.clear()


class ServerController(QWidget):
    """
    MVC pattern: Creates a controller - mvc pattern - just for the server.
    """

    def __init__(self, port, parent=None):
        """
        Constructor
        :param port: ServerPort
        :param parent:
        """
        super().__init__(parent)
        self.Form = ServerUI.ServerUI()
        self.Form.setupUi(self)
        self.signalHandler = SignalHandler()
        self.signalHandler.clearSignal.connect(self.Form.textBrowser.clear)
        self.signalHandler.newUser.connect(self.newUser)
        self.signalHandler.newmsg.connect(self.msg)
        self.model = Model.Server(self.Form,int(port),self.signalHandler)
        self.model.start()

    @Slot(str)
    def newUser(self, name):
        self.Form.textBrowser.append(name)

    @Slot(str)
    def msg(self, txt):
        self.Form.textBrowser_2.append(txt)

    def closeEvent(self, *args, **kwargs):
        """
        What to do, if the Window closes
        """
        self.model.running = False
        self.signalHandler.stop()




class MainController(QWidget):
    """
    MVC pattern: Creates a controller - mvc pattern - MainController for all.
    """

    cc = []
    sc = []
    ci = 0
    si = 0


    def __init__(self, parent=None):
        """
        Constructor
        :param parent:
        """
        super().__init__(parent)
        self.form = Start.Ui_Form()
        self.form.setupUi(self)
        self.form.cStart.clicked.connect(self.buttons)
        self.form.sStart.clicked.connect(self.buttons)
 
    def buttons(self):
        """
        The Event Method called from the clicked buttons .
        """
        button = self.sender()
        if button == self.form.cStart:
            MainController.cc.append(ClientController(self.form.cIP.text(), self.form.cName.text(), self.form.cPort.text()))
            MainController.cc[MainController.ci].show()
            MainController.ci += 1

        if button == self.form.sStart:
            MainController.sc.append(ServerController(self.form.sPort.text()))
            MainController.sc[MainController.si].show()
            MainController.si += 1

        self.show()


app = QApplication(sys.argv)
c = MainController()
c.show()
sys.exit(app.exec_())
