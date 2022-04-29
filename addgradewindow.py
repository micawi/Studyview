from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFileDialog;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;
from pickle import dump;
from gradeaddedmsg import GradeAddedMsg;
from errorwindow import ErrorWindow;
from grade import Grade;
import os;

class AddGradeWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    FontSize: int;
    Font: str;

    # Elements
    ModuleLbl: QLabel;
    GradeLine: QLineEdit;
    CPLbl: QLabel;
    CPLine: QLineEdit;
    AddGrdBtn: QPushButton;
    CancelBtn: QPushButton;

    # Subwindows
    GrdAddedMsg: GradeAddedMsg;
    ErrWindow: ErrorWindow;

    # Init
    def __init__(self, moduleToAdd: str, spacing: int):
        super().__init__();
        self.XSize = 300;
        self.YSize = 200;
        self.Font = "Calibri";
        self.FontSize = 10;
        self.Spacing = spacing;
        self.ModuleToAdd = moduleToAdd;

        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowModality(Qt.ApplicationModal);
        self.setFont(QFont(self.Font, self.FontSize));
        self.setWindowTitle("Add grade");

        self.ModuleLbl = QLabel(self);
        self.ModuleLbl.setText(moduleToAdd + ": ");
        width: int = self.ModuleLbl.width();
        height: int = self.ModuleLbl.height();
        self.ModuleLbl.move(int(self.Spacing/2), int(self.Spacing/2));

        self.GradeLine = QLineEdit(self);
        self.GradeLine.setMaxLength(4);
        width1: int = self.GradeLine.width();
        self.GradeLine.setFixedWidth(35);
        self.GradeLine.move(int(self.Spacing/2) + int(width * 1.5), int(self.Spacing/2));

        self.CPLbl = QLabel(self);
        self.CPLbl.setText("CP: ");
        self.CPLbl.move(int(self.Spacing/2) + int(width * 1.9), int(self.Spacing/2));

        self.CPLine = QLineEdit(self);
        self.CPLine.setMaxLength(2);
        self.CPLine.setFixedWidth(25);
        self.CPLine.move(int(self.Spacing/3) * 2 + width + width1, int(self.Spacing/2));

        self.AddGrdBtn = QPushButton("ADD GRADE", self);
        self.AddGrdBtn.move(int(self.Spacing/2), self.Spacing * 2);
        self.AddGrdBtn.setFixedWidth(self.XSize - self.Spacing);
        self.AddGrdBtn.clicked.connect(self.addGrade);

        self.CancelBtn = QPushButton("CANCEL", self);
        width = self.CancelBtn.width();
        self.CancelBtn.move(int(self.XSize/2) - int(width/2.75), int(self.Spacing * 2.5));
        self.CancelBtn.clicked.connect(self.cancel);

        self.show();
    
    # Adding of grade to specified file/location
    def addGrade(self):
        gradeName: str = self.ModuleLbl.text();
        gradeStr: str = self.GradeLine.text();
        cpStr: str = self.CPLine.text();

        if((gradeStr != "") & (cpStr != "")):
            grade: float = float(gradeStr);
            cp: int = int(cpStr);
            cwd: str = os.getcwd();
            usrData: str = cwd + "/userdata/";
            gradePath: str = usrData + gradeName + ".dat";

            if(not os.path.exists(usrData)):
                os.mkdir(usrData);
            
            if(not os.path.exists(gradePath)):
                with open(gradePath, "wb") as f:
                    grade = Grade(gradeName, grade, cp);
                    dump(grade, f);
            else:
                self.ErrWindow = ErrorWindow("ModuleExists", self.Font, self.FontSize, self.Spacing);
                return;
        else:
            self.ErrWindow = ErrorWindow("Empty", self.Font, self.FontSize, self.Spacing);
            return;

        self.GrdAddedMsg = GradeAddedMsg(self.Spacing);
        return;
    
    # Close on cancel
    def cancel(self):
        self.close();
