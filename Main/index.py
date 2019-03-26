import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
#provides necessary imports

class Example(QWidget):
#new class "Example" is created

    def __init__(self):
    #initialisation stuff
        super().__init__()
        #super returns parent object, __init__() is a constructor method in Python

        self.initUI()
        #gui created

    def initUI(self):
    #gui stuff
        QToolTip.setFont(QFont('SansSerif', 10))
        #font for tooltip
        self.setToolTip('This is a <b>QWidget</b> widget')
        #creates tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #creates button with tooltip
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        #button resized and moved, sizeHint gives recommended size

        self.setGeometry(300, 300, 300, 220)
        #locates and sets size of app, first two position, last two size width then height
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        #object QIcon created and receives path for icon

        self.show()

    def closeEvent(self, event):
    #when close button pressed stuff
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #first string is title of Message
        #second string is message text displayed
        #third argument specifies buttons displayed
        #last parameter is default (has keyboard focus)
        #value is stored in reply variable

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        #checks variable "reply"

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #app and example objects created
