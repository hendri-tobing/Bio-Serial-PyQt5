import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout,QDesktopWidget, QGroupBox)
from biostyle import *
from globalf import *
from kalorimeter import *

class page1(QWidget):
    
    def __init__(self):
        super(page1, self).__init__()
        self.initUI1()

    def initUI1(self):
        # ----Create first tab
        self.titlePage1 = QLabel(" Biology Experiment List")
        self.titlePage1.setStyleSheet(titlestyle)

        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.titlePage1)

        self.listLabel1 = QLabel('Calorimeter')
        self.listLabel2 = QLabel('')
        self.listLabel3 = QLabel('')

        picon1 = '001-temperature.png'
        picon = resource_path(os.path.join('src', picon1))

        hbox1 = QHBoxLayout()
        self.groupBox1 = QGroupBox('')
        hvbox1 = QVBoxLayout()
        self.groupBox1.setLayout(hvbox1)
        hvbox1.addWidget(self.listLabel1)
        hvbox1.addStretch(6)
        hhbox1 = QHBoxLayout()
        hhbox1.addStretch()
        self.goBtn1 = PicButton(QPixmap(picon))
        self.goBtn1.setToolTip('Click to Enter <b>Calorimeter</b> experiment!')
        hhbox1.addWidget(self.goBtn1)
        hhbox1.addStretch()
        hvbox1.addLayout(hhbox1)
        hvbox1.addStretch(3)
        hbox1.addStretch()
        hbox1.addWidget(self.groupBox1)
        hbox1.addStretch()
        layout1 = QVBoxLayout()
        layout1.addLayout(hbox0)
        layout1.addStretch(2)
        layout1.addLayout(hbox1)
        layout1.addStretch(3)
        self.setLayout(layout1)

        self.groupBox1.setStyleSheet(groupStyle)

        self.resize(972, 600)
        self.center()
        self.setWindowTitle('Biology Experiment') 
        winIcon1 = 'ico-bio.png'
        winIcon = resource_path(os.path.join('src', winIcon1))
        self.setWindowIcon(QIcon(winIcon))  
        self.show()

        self.goBtn1.clicked.connect(self.goBtn1Click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def goBtn1Click(self):
        self.form = page2()
        self.form.show()
        self.close()