import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib import animation as animation
from PyQt5.QtWidgets import QSizePolicy
import csv
from globalf import resource_path
import os

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        global fig

        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        #self.axes = fig.add_subplot(111)#, IYV: can be removed
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
        self.animate()


    def plot(self):
        global ax1
        style.use('ggplot')
        ax1 = self.figure.add_subplot(111)

    def  animate(self):
        self.anim = animation.FuncAnimation(fig, self.animate_loop, interval=1000)
        self.draw()

    def animate_loop(self, i):
        filename1='sensor_output.csv'
        filename = resource_path(os.path.join('src', filename1))
        pullData = open(filename,"r").read()
        dataArray = pullData.split('\n')
        xar = []
        yar1 = []
        yar2 = []
        yar3 = []
        yar4 = []
        for eachLine in dataArray:
            if len(eachLine)>1:
                x,y1,y2,y3,y4 = eachLine.split(',')
                xar.append(int(x))
                yar1.append(int(y1))
                yar2.append(int(y2))
                yar3.append(int(y3))
                yar4.append(int(y4))

        #print(dataArray)

        ax1.clear()
        ax1.plot(xar,yar1,label='Analog Temperature1',linewidth=2)
        ax1.plot(xar,yar2,label='Analog Temperature2',linewidth=2)
        ax1.plot(xar,yar3,label='Digital Temperature',linewidth=2)
        ax1.plot(xar,yar4,label='Humidity',linewidth=2)
        ax1.legend(loc="upper left")
