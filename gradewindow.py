from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton;


class GradeWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;

    # Elements
    Grid: QGridLayout;

    def __init__(self):
        super().__init__();
        