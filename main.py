from PyQt5.QtWidgets import QApplication;
from mainwindow import MainWindow;
import sys;

def main():
    app = QApplication(sys.argv);
    mainWindow = MainWindow(app);
    app.exec_();

main();