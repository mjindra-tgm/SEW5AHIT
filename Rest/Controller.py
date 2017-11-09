from PySide.QtCore import *
from PySide.QtGui import *
import View
import sys
import requests
from xml.etree import ElementTree



class Controller(QWidget):

     def __init__(self, parent=None):
         super().__init__(parent)
         self.myForm = View.Ui_Form()
         self.myForm.setupUi(self)


     def reset(self):
        print("reset")

     def submit(self):

         anweisung=""
         duration=""

         url = "http://maps.googleapis.com/maps/api/directions/xml"
         params = {"origin": self.myForm.lineEdit.text(),
                "destination": self.myForm.lineEdit_2.text(),
                "sensor": "false",
                "language":"de"}
         res = requests.get(url, params)
         root = ElementTree.fromstring(res.content)

         for child in root.iter('html_instructions'):
            anweisung += child.text + "<br>"

         self.myForm.ergebnis.setHtml(str(anweisung))



if __name__ == "__main__":
 app = QApplication(sys.argv)
 c = Controller()
 c.show()
 sys.exit(app.exec_())