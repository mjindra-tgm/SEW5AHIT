from xml.etree import ElementTree

from PySide.QtGui import *
import requests
import view
import sys

class Controller(QWidget):

    def __init__(self, parent=None):
        """
        Der Konstruktor
        """
        super().__init__(parent)
        self.myForm = view.Ui_Form()
        self.myForm.setupUi(self)

    def submit(self):
        headers = headers = {"content-type": "application/json"}
        params = {"origin": self.myForm.start, "destination": self.myForm.ziel, "language": "de", "sensor": "false"}
        res = requests.get("http://maps.googleapis.com/maps/api/directions/json", params, headers=headers)
        instructions = ""
        res2 = res.json()
        for key in res2["duration"]:
            instructions += key

        self.myForm.textBrowser.setHtml(instructions)

    def reset(self):
        self.myForm.start.setText("")
        self.myForm.ziel.setText("")
        self.myForm.textBrowser.setHtml("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())