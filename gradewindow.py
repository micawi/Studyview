from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QFrame;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;
from grade import Grade;
from errorwindow import ErrorWindow;
import os, pickle;


class GradeWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Font: str;
    FontSize: int;
    Spacing: int;
    
    GradeList: list;
    NameValList: list;
    GradeValList: list;
    CPValList: list;

    # Elements
    Grid: QGridLayout;
    SepFrame: QFrame;

    NameLbl: QLabel;
    GradeLbl: QLabel;
    CPLbl: QLabel;

    # Subwindows
    ErrWindow: ErrorWindow;

    # Init
    def __init__(self, font: str, fontsize: int, spacing: int):
        super().__init__();
        self.XSize = 440;
        self.YSize = 200;
        self.Font = font;
        self.FontSize = fontsize;
        self.Spacing = spacing;
        self.GradeList = [];

        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowModality(Qt.ApplicationModal);
        self.setFont(QFont(self.Font, self.FontSize));
        self.setWindowTitle("Show grades");

        self.NameLbl = QLabel(self);
        self.NameLbl.setText("Module name");
        width: int = self.NameLbl.width();
        self.NameLbl.move(self.Spacing, self.Spacing);
        
        self.GradeLbl = QLabel(self);
        self.GradeLbl.setText("Grade");
        self.GradeLbl.move(self.Spacing + int(width * 2), self.Spacing);

        self.CPLbl = QLabel(self);
        self.CPLbl.setText("CP");
        self.CPLbl.move(self.Spacing + int(width * 3), self.Spacing);

        self.SepFrame = QFrame(self);
        self.SepFrame.setFrameShape(QFrame.HLine);
        self.SepFrame.move(self.Spacing, int(self.Spacing * 1.35));
        self.SepFrame.setFixedSize(400 - int(self.Spacing * 1.3), 1);

        hasGrades: bool = self.getGrades();
        if(hasGrades): # Init of grades from userdata for GUI display as Labels
            grade: Grade;
            self.NameValList = [];
            self.GradeValList = [];
            self.CPValList = [];
            currNameValLbl: QLabel;
            currGradeValLbl: QLabel;
            currCPValLbl: QLabel;

            for grade in self.GradeList:
                currNameValLbl = QLabel(self);
                currNameValLbl.setText(grade.ModuleName);
                currGradeValLbl = QLabel(self);
                currGradeValLbl.setText(str(grade.Grade));
                currCPValLbl = QLabel(self);
                currCPValLbl.setText(str(grade.CP));

                self.NameValList.append(currNameValLbl);
                self.GradeValList.append(currGradeValLbl);
                self.CPValList.append(currCPValLbl);

            for i in range(len(self.GradeList)):
                self.NameValList[i].move(self.Spacing, self.Spacing + int(self.Spacing/2) * (i + 1));
                self.GradeValList[i].move(self.Spacing + int(width * 2), self.Spacing + int(self.Spacing/2) * (i + 1));
                self.CPValList[i].move(self.Spacing + int(width * 3), self.Spacing + int(self.Spacing/2) * (i + 1));
                self.YSize += int(self.Spacing/2) * i;
                self.setFixedSize(self.XSize, self.YSize);             
            
            self.show();

    # Get grades from userdata
    def getGrades(self) -> bool:
        cwd: str = os.getcwd();
        usrData: str = cwd + "/userdata/";
        allFiles: list = os.listdir(usrData);
        
        if(allFiles != []):
            fileName: str;
            for fileName in allFiles:
                currFile: str = usrData + fileName;
                with open(currFile, "rb") as f:
                    currGrade: Grade = pickle.load(f);
                    self.GradeList.append(currGrade);
        else:
            self.ErrWindow = ErrorWindow("NoGrades", self.Font, self.FontSize, self.Spacing);
            return False;
        
        return True;