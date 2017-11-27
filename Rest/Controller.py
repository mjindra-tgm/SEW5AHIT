from PySide.QtCore import *
from PySide.QtGui import *
import View
import sys
import requests
from xml.etree import ElementTree



class Controller(QWidget):
     """
     Der Controller der Verbindung zu dem Model(Rest) und dem View Teil des MVC'S aufbaut
     """

     def __init__(self, parent=None):
         """
         Der Konstruktor
         """
         super().__init__(parent)
         self.myForm = View.Ui_Form()
         self.myForm.setupUi(self)


     def reset(self):
        """
        Diese Methode stellt die urpsrüngliche GUI ohne Input/Output wieder her.
        """
        self.myForm.lineEdit.clear()
        self.myForm.lineEdit_2.clear()
        self.myForm.ergebnis.clear()

     def submit(self):
         """
         Diese Methode nimmt den Input der View entgegen und gibt ihn an das Model(Rest Service, Google Maps Directions API) weiter. Der Output kommt wieder zurück in die View
         """

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
         start_address=""
         end_address = ""

         root  = ElementTree.fromstring(res.content)
         error=""

         for child in root.iter('status'):
            if child.text == "NOT_FOUND" or child.text == "ZERO_RESULTS":
                error = "<b>Der Abfahrt-/Ankunftsort ist nicht vorhanden</b>"

         for child in root.iter('start_address'):
            start_address += "Ihre <b>Fahrtzeit</b> von <b>" + child.text

         for child in root.iter('end_address'):
            end_address += "</b> bis  <b>" + child.text

         for child in root.iter('duration'):
            duration = "</b> beträgt <b>" + child.find("text").text

         for child in root.iter('distance'):
            distance = "</b> auf einer <b>Länge</b> von <b>" + child.find("text").text + "</b><br>"


         for child in root.iter('html_instructions'):
            anweisung += child.text + "<br>"

         self.myForm.ergebnis.setHtml(error+start_address+end_address+duration+distance+str(anweisung))



if __name__ == "__main__":
 app = QApplication(sys.argv)
 c = Controller()
 c.show()
 sys.exit(app.exec_())