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
        self.myForm.lineEdit.clear()
        self.myForm.lineEdit_2.clear()
        self.myForm.ergebnis.clear()

     def submit(self):

         anweisung=""
         duration=""

         url = "http://maps.googleapis.com/maps/api/directions/xml"
         params = {"origin": self.myForm.lineEdit.text(),
                "destination": self.myForm.lineEdit_2.text(),
                "sensor": "false",
                "language":"de"}
         res = requests.get(url, params)

         duration=""
         distance=""

         root  = ElementTree.fromstring(res.content)
         for child in root.iter('duration'):
            duration = "Ihre Fahrtzeit beträgt <b>" + child.find("text").text

         for child in root.iter('distance'):
            destination = "</b> auf einer Länge von <b>" + child.find("text").text + "</b><br>"

         print(duration)

         for child in root.iter('html_instructions'):
            anweisung += child.text + "<br>"

         self.myForm.ergebnis.setHtml(duration+destination+str(anweisung))



if __name__ == "__main__":
 app = QApplication(sys.argv)
 c = Controller()
 c.show()
 sys.exit(app.exec_())