from PyQt5.QtWidgets import QDesktopWidget, QAbstractButton
from PyQt5.QtGui import QPainter
import sys, os

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        data_dir = sys._MEIPASS
        return os.path.join(data_dir, relative)
    return os.path.join(relative)


def center(self):
    
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()