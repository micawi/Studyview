from PyQt5.QtWidgets import QWidget, QLabel, QPushButton;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;

class GradeAddedMsg(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    Font: int;
    FontSize: str;

    # Elements
    TextLbl: QLabel;
    OkBtn: QPushButton;

    # Init
    def __init__(self, spacing: int):
        super().__init__();
        self.XSize = 250;
        self.YSize = 150;
        self.Spacing = spacing;
        self.Font = "Calibri";
        self.FontSize = 10;

        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowModality(Qt.ApplicationModal);
        self.setFont(QFont(self.Font, self.FontSize));
        self.setWindowTitle("Grade added");

        self.TextLbl = QLabel(self);
        self.TextLbl.setText("Grade successfully added.");
        width: int = self.TextLbl.width();
        height: int = self.TextLbl.height();
        self.TextLbl.move(int(self.XSize/2) - int(width/1.5), int(self.YSize/2) - height);

        self.OkBtn = QPushButton("OK", self);
        self.OkBtn.move(int(self.XSize/2) - int(width/3), self.YSize - int(self.Spacing));
        self.OkBtn.clicked.connect(self.accept);

        self.show();

    # Close on OK
    def accept(self):
        self.close();