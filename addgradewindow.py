from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;

class AddGradeWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    FontSize: int;
    Font: str;

    # Elements


    # Init
    def __init__(self, moduleToAdd: str):
        super().__init__();
