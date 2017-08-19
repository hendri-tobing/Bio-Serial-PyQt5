import sys
#import time
from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QComboBox, QDesktopWidget, QMessageBox, QFileDialog)
from shutil import copyfile
from biostyle import *
from biovar import *
from animplot import *
from bioserial import *
from writefile import writef

class page2(QWidget):
    def __init__(self):
        super(page2, self).__init__()
        self.initUI2()

    def initUI2(self):
        self.titlePage2 = QLabel(" Calorimenter")
        self.titlePage2.setStyleSheet(titlestyle)
        self.portLabel = QLabel('Port: ')
        self.portCombox = QComboBox()
        self.refreshButton = QPushButton('Refresh Port')
        self.conButton = QPushButton('Measure')
        self.downLoad = QPushButton('Reset and Save Data')
        self.refreshButton.clicked.connect(self.refreshed)
        self.conButton.clicked.connect(self.conSerial)
        self.downLoad.clicked.connect(self.savefile)

        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.titlePage2)

        self.atemLabel1 = QLabel('Analog Temperature1')
        self.atemLabel2 = QLabel('Analog Temperature2')
        self.dtemLabel = QLabel('Digital Temperature')
        self.dhumLabel = QLabel('Digital Humidity')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.portLabel)
        hbox1.addWidget(self.portCombox)
        hbox1.addWidget(self.refreshButton)
        hbox1.addWidget(self.conButton)
        hbox1.addStretch()
        hbox1.addWidget(self.downLoad)

        hbox2 = QHBoxLayout()
        self.groupBox1 = QGroupBox('')
        hvbox1 = QVBoxLayout()
        self.groupBox1.setLayout(hvbox1)
        hvbox1.addWidget(self.atemLabel1)
        hvbox1.addStretch(6)
        hhbox1 = QHBoxLayout()
        hhbox1.addStretch()
        self.atemVal1 = QLabel(str(y1) +  ' °' )
        hhbox1.addWidget(self.atemVal1)
        hhbox1.addStretch()
        hvbox1.addLayout(hhbox1)
        hvbox1.addStretch(3)

        self.groupBox2 = QGroupBox('')
        hvbox2 = QVBoxLayout()
        self.groupBox2.setLayout(hvbox2)
        hvbox2.addWidget(self.atemLabel2)
        hvbox2.addStretch(6)
        hhbox2 = QHBoxLayout()
        hhbox2.addStretch()
        self.atemVal2 = QLabel(str(y2) +  ' °' )
        hhbox2.addWidget(self.atemVal2)
        hhbox2.addStretch()
        hvbox2.addLayout(hhbox2)
        hvbox2.addStretch(3)

        self.groupBox3 = QGroupBox('')
        hvbox3 = QVBoxLayout()
        self.groupBox3.setLayout(hvbox3)
        hvbox3.addWidget(self.dtemLabel)
        hvbox3.addStretch(6)
        hhbox3 = QHBoxLayout()
        hhbox3.addStretch()
        self.dtemVal = QLabel(str(y3) +  ' °' )
        hhbox3.addWidget(self.dtemVal)
        hhbox3.addStretch()
        hvbox3.addLayout(hhbox3)
        hvbox3.addStretch(3)

        self.groupBox4 = QGroupBox('')
        hvbox4 = QVBoxLayout()
        self.groupBox4.setLayout(hvbox4)
        hvbox4.addWidget(self.dhumLabel)
        hvbox4.addStretch(6)
        hhbox4 = QHBoxLayout()
        hhbox4.addStretch()
        self.dhumVal = QLabel(str(y4) +  ' %' )
        hhbox4.addWidget(self.dhumVal)
        hhbox4.addStretch()
        hvbox4.addLayout(hhbox4)
        hvbox4.addStretch(3)

        hbox2.addWidget(self.groupBox1)
        hbox2.addWidget(self.groupBox2)
        hbox2.addWidget(self.groupBox3)
        hbox2.addWidget(self.groupBox4)

        m = PlotCanvas(self, width =5, height=4)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(m)

        self.layout2 = QVBoxLayout(self)
        self.layout2.addLayout(hbox0)
        self.layout2.addLayout(hbox1)
        self.layout2.addLayout(hbox2)
        self.layout2.addLayout(hbox3)
        self.setLayout(self.layout2)

        self.atemLabel1.setStyleSheet(labelColStyle)
        self.atemLabel2.setStyleSheet(labelColStyle)
        self.dtemLabel.setStyleSheet(labelColStyle)
        self.dhumLabel.setStyleSheet(labelColStyle)

        self.atemVal1.setStyleSheet(valStyle)
        self.atemVal2.setStyleSheet(valStyle)
        self.dtemVal.setStyleSheet(valStyle)
        self.dhumVal.setStyleSheet(valStyle)

        self.groupBox1.setStyleSheet(groupStyle)
        self.groupBox2.setStyleSheet(groupStyle)
        self.groupBox3.setStyleSheet(groupStyle)
        self.groupBox4.setStyleSheet(groupStyle)

        #---serial port list
        def comboPortList(portCombo):
            ports = serial_ports()
            try:
                for port in range(len(ports)):
                    try:
                        portCombo.addItem(ports[port])
                    finally:
                        pass
            finally:
                pass
        comboPortList(self.portCombox)
       
        #reset file
        src1 = 'sensor_output.csv'
        src = resource_path(os.path.join('src', src1))
        src2a = 'sensor_output_ori.csv'
        src2 = resource_path(os.path.join('src', src2a))
        copyfile(src2, src)
   
        self.resize(972, 600)
        self.center()
        self.setWindowTitle('Biology Experiment')
        winIcon1 = 'ico-bio.png'
        winIcon = resource_path(os.path.join('src', winIcon1))
        self.setWindowIcon(QIcon(winIcon))  
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def refreshed(self):
        ports = serial_ports()
        self.portCombox.clear()
        try:
            for port in range(len(ports)):
                self.portCombox.addItem(ports[port])
        finally:
            pass

    def savefile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)
 
        src1 = 'sensor_output.csv'
        src = resource_path(os.path.join('src', src1))
        dst = fileName+'.csv'
        buttonReply = QMessageBox.question(self, 'Save file', "Save file at "+ dst +" ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            copyfile(src, dst)
            print("File was saved at " + dst)
            QMessageBox.about(self, "Info", "File was saved at " + dst)
            src2a = 'sensor_output_ori.csv'
            src2 = resource_path(os.path.join('src', src2a))
            copyfile(src2, src)
            global loopz
            loopz = 0
        elif buttonReply == QMessageBox.No:
            pass
        else:
            print('No clicked.')

    def conSerial(self):
        global loopz
        port_serial = self.portCombox.currentText()
        try:       
            if self.conButton.text() == 'Measure' and port_serial != '':
                print('open1')
                ser = SerialWrapper1(port_serial)
                sercon1 = ser.sercon1()
                if sercon1 == "OK":
                    data = ser.serrun1()
                    self.setTextVal(data)
                    ser.serclose()
                    data.insert(0, loopz)
                    writef(data)
                    loopz = loopz + 1         
                else:
                    QMessageBox.about(self, "Error2!", "Error2, check the usb connection, then click 'Refresh Port'")
                    ser.serclose()
                    self.conButton.setText('Measure')
            else:
                QMessageBox.about(self, "Error3!", "Error3, check the usb connection, then click 'Refresh Port'")
        except Exception as ex:
            QMessageBox.about(self, "Error1!", "Error1, check the usb connection, then click 'Refresh Port'")
            print(ex)
        finally:
            pass

    def setTextVal(self, data):
        self.atemVal1.setText((data[0]) +  ' °' )
        self.atemVal2.setText((data[1]) +  ' °' )
        self.dtemVal.setText((data[2]) +  ' °' )
        self.dhumVal.setText((data[3]) +  ' %' )