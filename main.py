from PyQt5.QtWidgets import QApplication;
from mainwindow import MainWindow;
import sys;

app = QApplication(sys.argv);
mainWindow = MainWindow();
app.exec_();