import os
import serial
import sys
from globalf import *

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        import glob
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        import glob
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class SerialWrapper1:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate = 19200, timeout=0.5, write_timeout = 1)

    def sercon1(self):
        message = b'1\r\n'
        sentval = "null"
        try:
            print('open port')
            self.ser.write(message)
            resp1=self.ser.readline()
            resp2=self.ser.readline()
            resp = resp1.decode("utf-8") + resp2.decode("utf-8")
            print('resp = ' + resp)
            if "OK" in resp:
                sentval = "OK"
            else:
                self.ser.close()
        except Exception as ex:
            print('Error Serial2')
            print(ex)
        finally:
            return sentval
        
    def serrun1(self):
        data="null"
        self.ser.write(b'g')
        valraw=self.ser.readline()
        val = valraw.decode("utf-8").rstrip()
        print('raw value: ' + val)
        self.ser.write(b'x')
        rawclose1=self.ser.readline()
        rawclose2=self.ser.readline()
        rawclose = rawclose1.decode("utf-8") + rawclose2.decode("utf-8")
        print('rawclose = ' + rawclose)
        if "v4" in val:
            values = val.split(' ')
            if len(values)==4:
                value0 = values[0][3:]
                value1 = values[1][3:]
                value2 = values[2][3:]
                value3 = values[3][3:]
                data=[value0, value1, value2, value3]
            else:
                pass
        return data

    def serclose(self):
        self.ser.close()