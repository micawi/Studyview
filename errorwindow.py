from PyQt5.QtWidgets import QWidget, QLabel, QPushButton;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;


class ErrorWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    Font: str;
    FontSize: int;

    # Elements
    ErrMsgLbl: QLabel;
    OkBtn: QPushButton;

    # Init
    def __init__(self, errType: str, font: str, fontSize: int, spacing: int):
        super().__init__();
        self.XSize = 300;
        self.YSize = 150;
        self.Font = font;
        self.FontSize = fontSize;
        self.Spacing = spacing;
        
        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowModality(Qt.ApplicationModal);
        self.setFont(QFont(self.Font, self.FontSize));
        self.setWindowTitle(errType + " Error");

        self.ErrMsgLbl = QLabel(self);
        
        self.OkBtn = QPushButton("OK", self);
        width: int = self.OkBtn.width();
        height: int = self.OkBtn.height();
        self.OkBtn.move(int(self.XSize/2) - int(width/3), self.YSize - self.Spacing);
        self.OkBtn.clicked.connect(self.closeWindow);
        
        if(errType == "NoInput"):      
            self.ErrMsgLbl.setText("Enter a module name");
            width: int = self.ErrMsgLbl.width();
            height: int = self.ErrMsgLbl.height();
            self.ErrMsgLbl.move(int(self.XSize/2) - int(width/1.4), int(self.YSize/2) - height);
        elif(errType == "WrongInput"):
            self.ErrMsgLbl.setText("Invalid input given");
            width: int = self.ErrMsgLbl.width();
            height: int = self.ErrMsgLbl.height();
            self.ErrMsgLbl.move(int(self.XSize/2) - int(width/1.4), int(self.YSize/2) - height);            
        elif(errType == "ModuleExists"):
            self.ErrMsgLbl.setText("Module already exists");
            width: int = self.ErrMsgLbl.width();
            height: int = self.ErrMsgLbl.height();
            self.ErrMsgLbl.move(int(self.XSize/2) - int(width/1.4), int(self.YSize/2) - height);
        elif(errType == "Empty"):
            self.ErrMsgLbl.setText("Enter grade and CP");
            width: int = self.ErrMsgLbl.width();
            height: int = self.ErrMsgLbl.height();
            self.ErrMsgLbl.move(int(self.XSize/2) - int(width/1.4), int(self.YSize/2) - height);
        elif(errType == "NoGrades"):
            self.ErrMsgLbl.setText("No grades stored");
            width: int = self.ErrMsgLbl.width();
            height: int = self.ErrMsgLbl.height();
            self.ErrMsgLbl.move(int(self.XSize/2) - int(width/1.55), int(self.YSize/2) - height); 

        self.show();
    
    # Close window on ok
    def closeWindow(self):
        self.close();