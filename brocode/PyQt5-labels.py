import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(600,300,500,500)
        self.setWindowIcon(QIcon("brocode/GUI-logo.jpeg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: black;"
                            "background-color: white;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration: underline;"
                            )
        # label.setAlignment(Qt.AlignTop) #Vertically top
        # label.setAlignment(Qt.AlignBottom) #Vertically buttom
        # label.setAlignment(Qt.AlignVCenter) #Vertically center
        # label.setAlignment(Qt.AlignRight)  #Horizontally right
        # label.setAlignment(Qt.AlignLeft) #Horizontally left
        # label.setAlignment(Qt.AlignHCenter)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center and Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center and Bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center or Qt.AlignCenter(same usage)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()