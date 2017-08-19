import os
from PyQt5.QtWidgets import QApplication, QSplashScreen, QProgressBar

from lists import *
from globalf import *

if __name__ ==  '__main__':
    import sys, time
    
    app = QApplication(sys.argv)
    # Create and display the splash screen
    splash_pic1 = '12.jpg'
    splash_pic = resource_path(os.path.join('src', splash_pic1))
    splash_pix = QPixmap(splash_pic)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # adding progress bar
    progressBar = QProgressBar(splash)
    splash.setMask(splash_pix.mask())


    splash.show()
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.01:
           app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    form = page1()
    form.show()
    splash.finish(form)
    app.exec_()    




