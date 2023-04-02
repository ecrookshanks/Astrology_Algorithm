import sys                        # needed for the sys.argv passed to QApplication below (command line arguments)

from PyQt6.QtWidgets import QDialog, QApplication, QColorDialog, QMainWindow
from PyQt6.QtGui import QColor, QPalette
from PyQt6.uic import loadUi      # special library to load .ui file directly


signs = ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces')


class MyForm(QMainWindow):
    # constructor for this MyForm class 
    def __init__(self):
        super().__init__()   # calls the constructor of the QDialog class that is inherited
        
        # Change 'gui_template.ui' to the .ui file you created with Qt Designer
        # or rename the provided gui_template.ui to your own file and change name
        # the .ui file MUST BE IN THE SAME FOLDER AS THIS .PY FILE
        self.ui = loadUi('main_1.ui', self)   #<======= this line must be changed to your .UI file!
        
        self.ui.signList.addItem('Aries')
        self.ui.signList.addItem('Taurus')
        self.ui.signList.addItem('Gemini')
        self.ui.signList.addItem('Cancer')
        self.ui.signList.addItem('Leo')
        self.ui.signList.addItem('Virgo')
        self.ui.signList.addItem('Libra')
        self.ui.signList.addItem('Scorpio')
        self.ui.signList.addItem('Sagittarius')
        self.ui.signList.addItem('Capricorn')
        self.ui.signList.addItem('Aquarius')
        self.ui.signList.addItem('Pisces')
        
        
        self.ui.signList.currentTextChanged.connect(self.sign_changed)
        self.ui.signList.setCurrentIndex(-1)
        
        # self.ui.actionColor.triggered.connect(self.menuBackgroundMethod)
        # self.ui.actionExit.triggered.connect(self.exitMethod)
        # self.ui.pushButton5.clicked.connect(self.fiveMinutes)
        # add code here to connect the pushButton widgets to your methods.
        # for this first project three empty methods are already created.
        # you are responsible for connecting the clicked signal from your widgets
        self.show()   # this line shows the .ui file after all the Widget's signals are connected.

    def menuBackgroundMethod(self):
        intial_color = self.ui.menubar.palette().color(QPalette.Foreground)
        color = QColorDialog.getColor(intial_color, self, "Pick a color!")
        color1 = QColor("Red")

        if color.isValid():
            pal = self.palette()
            pal.setColor(self.ui.backgroundRole(), color)
            self.setPalette(pal)
    
    def sign_changed(self, s):
      print("Changed to: " + s)
      
      try:
        orig = signs.index(s.lower())
      except:
        return
      
      spouseIndex = (orig + 6) % 12
      spouseWorkIndex = (orig + 6 + 5) % 12
      spouseCareerIndex = (orig + 6 + 5 + 4) % 12
      kidIndex = (orig + 4) % 12
      kidWorkIndex = (orig + 4 + 5) % 12

      self.ui.lblSubject.setText(s + ': (1)')
      self.ui.lblSpouse.setText(signs[spouseIndex].capitalize() + ' (7)' )
      self.ui.lblSpouseWork.setText(signs[spouseWorkIndex].capitalize() + ' (12)' )

    def exitMethod(self):
        QApplication.instance().quit()



# the code below should not be changed and is constant for all GUI programs
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    # w.show()            # not needed because constructor does .show()
    sys.exit(app.exec())  # note - sys.exit causes traceback in some editors if it does in yours just use app.exec()