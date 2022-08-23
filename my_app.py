#import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
#create app
app = QAplication([])

# напиши здесь код основного приложения и первого экрана
class Main_Win(QWidget):
    def initUI(self):
        #show win
        self.show()
        
        # #create txt
        # self.hello_text = QLabel(txt_hello) 
        # #create txt
        # self.instruction = QLabel(txt_instruction) 
        # #create button
        # self.button = QPushButton(txt_next)
        
        #create lines
        self.h_line_ht = QHBoxLayout()
        self.h_line_ins = QHBoxLayout()
        self.h_line_but = QHBoxLayout()
        self.v_line = QVBoxLayout()

#import txt instr
from instr import *
class Main_Win(QWidget):
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)


#method connect
# class Main_Win(QWidget):
#     def connects(self)
#     self.btn_next.clicked.connect(self.next_click)


        #method connect
class Main_Win(QWidget):
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
#create def next_click
class Main_Win(QWidget):
    def next_click.(self):
        #hide the win
        self.hide()

from second_win import *
class Main_Win(QWidget):
    def next_click(self):
        self.hide()
        self.tw = TestWin()

        

#keep app open
app.exec_()