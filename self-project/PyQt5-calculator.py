#Creating a function calculator by using PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import Qt

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.result_output = QLabel("0", self)

        #set up labels for button
        self.delete_button = QPushButton("⌦", self)
        self.all_clear_button = QPushButton("AC", self)
        self.mod_button = QPushButton("%", self)
        self.divide_button = QPushButton("÷", self)
        self.seven_button = QPushButton("7", self)
        self.eight_button = QPushButton("8", self)
        self.nine_button = QPushButton("9", self)
        self.multiple_button = QPushButton("x", self)
        self.four_button = QPushButton("4", self)
        self.five_button = QPushButton("5", self)
        self.six_button = QPushButton("6", self)
        self.minus_button = QPushButton("-", self)
        self.one_button = QPushButton("1", self)
        self.two_button = QPushButton("2", self)
        self.three_button = QPushButton("3", self)
        self.add_button = QPushButton("+", self)
        self.positive_negative_button = QPushButton("+/-", self)
        self.zero_button = QPushButton("0", self)
        self.decimal_button = QPushButton(".", self)
        self.equal_button = QPushButton("=", self)


        
        self.initUI() #set up UI interface

    def initUI(self):
        self.setWindowTitle("Calculator App")

        #set minimal window size
        self.setMinimumSize(320, 200)


        main_layout = QVBoxLayout()
        button = QGridLayout()
        button.addWidget(self.result_output, 0, 0, 1, 4)
        button.addWidget(self.delete_button, 1, 0)
        button.addWidget(self.all_clear_button, 1, 1)
        button.addWidget(self.mod_button , 1, 2)
        button.addWidget(self.divide_button, 1, 3)
        button.addWidget(self.seven_button, 2, 0)
        button.addWidget(self.eight_button, 2, 1)
        button.addWidget(self.nine_button, 2, 2)
        button.addWidget(self.multiple_button, 2, 3)
        button.addWidget(self.four_button, 3, 0)
        button.addWidget(self.five_button, 3, 1)
        button.addWidget(self.six_button, 3, 2)
        button.addWidget(self.minus_button, 3, 3)
        button.addWidget(self.one_button, 4, 0)
        button.addWidget(self.two_button, 4, 1)
        button.addWidget(self.three_button, 4, 2)
        button.addWidget(self.add_button , 4, 3)
        button.addWidget(self.positive_negative_button, 5, 0)
        button.addWidget(self.zero_button, 5, 1)
        button.addWidget(self.decimal_button, 5, 2)
        button.addWidget(self.equal_button, 5, 3)

        #set objects
        self.result_output.setObjectName("result_output")
        self.delete_button.setObjectName("delete_button")
        self.all_clear_button.setObjectName("all_clear_button")
        self.mod_button.setObjectName("mod_button")
        self.divide_button.setObjectName("divide_button")
        self.seven_button.setObjectName("seven_button")
        self.eight_button.setObjectName("eight_button")
        self.nine_button.setObjectName("nine_button")
        self.multiple_button.setObjectName("multiple_button")
        self.four_button.setObjectName("four_button")
        self.five_button.setObjectName("five_button")
        self.six_button.setObjectName("six_button")
        self.minus_button.setObjectName("minus_button")
        self.one_button.setObjectName("one_button")
        self.two_button.setObjectName("two_button")
        self.three_button.setObjectName("three_button")
        self.add_button.setObjectName("add_button")
        self.positive_negative_button.setObjectName("positive_negative_button")
        self.zero_button.setObjectName("zero_button")
        self.decimal_button.setObjectName("decimal_button")
        self.equal_button.setObjectName("equal_button")

        self.setStyleSheet("""
            QPushButton{
                font-family: Arial;
                font-size: 30px;
                border-radius: 10px;
                color: white;
            }
            QPushButton#delete_button{
                background-color:grey;
            }
            QPushButton#all_clear_button{
                background-color: grey;
            }
            QPushButton#mod_button{
                background-color: grey;
            }
            QPushButton#divide_button{
                background-color: orange;
            }
            QPushButton#seven_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#eight_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#nine_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#multiple_button{
                background-color: orange;
            }
            QPushButton#four_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#five_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#six_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#minus_button{
                background-color: orange;
            }
            QPushButton#one_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#two_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#three_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#add_button{
                background-color: orange;
            }
            QPushButton#positive_negative_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#zero_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#decimal_button{
                background-color: hsl(0, 1%, 23%);
            }
            QPushButton#equal_button{
                background-color: orange;
            }
        """)

        self.result_output.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(button)

        #fix the layout of main window
        button.setRowStretch(0, 0)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

        #number clicks
        self.one_button.clicked.connect(lambda:self.number_click("1"))
        self.two_button.clicked.connect(lambda:self.number_click("2"))
        self.three_button.clicked.connect(lambda:self.number_click("3"))
        self.four_button.clicked.connect(lambda:self.number_click("4"))
        self.five_button.clicked.connect(lambda:self.number_click("5"))
        self.six_button.clicked.connect(lambda:self.number_click("6"))
        self.seven_button.clicked.connect(lambda:self.number_click("7"))
        self.eight_button.clicked.connect(lambda:self.number_click("8"))
        self.nine_button.clicked.connect(lambda:self.number_click("9"))
        self.zero_button.clicked.connect(lambda:self.number_click("0"))
        self.all_clear_button.clicked.connect(self.all_clear)

        #symbol clicks
        self.mod_button.clicked.connect(lambda:self.operation_symbols("%"))
        self.divide_button.clicked.connect(lambda:self.operation_symbols("÷"))
        self.add_button.clicked.connect(lambda:self.operation_symbols("+"))
        self.multiple_button.clicked.connect(lambda:self.operation_symbols("x"))
        self.minus_button.clicked.connect(lambda:self.operation_symbols("-"))

        #functional outputs
        self.delete_button.clicked.connect(self.delete)
        self.equal_button.clicked.connect(self.equal)
        self.positive_negative_button.clicked.connect(self.positive_negative)
        self.decimal_button.clicked.connect(self.decimal)

    def number_click(self, text):
        current_output = self.result_output.text()
        
        if current_output == "0":
            self.result_output.setText(text)
        else:
            self.result_output.setText(current_output + text)
        
    def delete(self):
        if self.result_output.text() == '0':
            pass
        else:
            current_output = self.result_output.text()
            new_result_output = current_output[:-1]
            self.result_output.setText(new_result_output)

    
    def all_clear(self):
        self.result_output.setText("0")

    def operation_symbols(self, symbol):
        current_output = self.result_output.text()
        self.result_output.setText(current_output + symbol)

    def equal(self):
        #find the index of symbols
        result = 0
        symbol_index = 0
        current_output = self.result_output.text()
        for i in range(len(current_output)):
            if current_output[i] == "%" or current_output[i] == "÷" or current_output[i] == "x" or current_output[i] == "+" or current_output[i] == "-":
                symbol_index = i
        
        first_half = float(current_output[:symbol_index])
        second_half = float(current_output[symbol_index+1:])

        if current_output[symbol_index] == "%":
            if second_half == 0:
                self.result_output.setText(current_output + " = Undefined")
                return
            result = first_half % second_half
        elif current_output[symbol_index] == "÷":
            if second_half == 0:
                self.result_output.setText(current_output + " = Undefined")
                return
            result = first_half / second_half
        elif current_output[symbol_index] == "x":
            result = first_half * second_half
        elif current_output[symbol_index] == "+":
            result = first_half + second_half
        else:
            result = first_half - second_half

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        self.result_output.setText(current_output + " = " + str(result))
        

        
    def positive_negative(self):
        current_output = self.result_output.text()
        if current_output[0] == "-":
            self.result_output.setText(current_output[1:])
        elif current_output == "0":
            return
        else:
            self.result_output.setText("-" + current_output)

    def decimal(self):
        is_decimal = False
        is_symbol = False #avoid second half decimal issue
        current_output = self.result_output.text()

        for i in range(len(current_output)):
            if current_output[i] == "%" or current_output[i] == "÷" or current_output[i] == "x" or current_output[i] == "+" or current_output[i] == "-":
                is_symbol = True
            if current_output[i] == ".":
                is_decimal = True
        
        if is_decimal and not is_symbol:
            return
        
        self.result_output.setText(current_output + ".")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator_app = calculator()
    calculator_app.show()
    sys.exit(app.exec_())

