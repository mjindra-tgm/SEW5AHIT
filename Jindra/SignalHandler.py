from PySide.QtCore import QObject
from PySide.QtCore import Signal


class SignalHandler(QObject):

    clearSignal = Signal()
    newUser = Signal(str)
    stopSignal = Signal()
    refreshSignal = Signal()
    stopCon = Signal(int)
    newmsg = Signal(str)

    def __init__(self):
        QObject.__init__(self)

    def clear(self):
        self.clearSignal.emit()

    def new_User(self,name):
        self.newUser.emit(name)

    def stop(self):
        self.stopSignal.emit()

    def refresh(self):
        self.refreshSignal.emit()

    def stopConnection(self, i):
        self.stopCon.emit(i)

    def msg(self,text):
        self.newmsg.emit(text)
