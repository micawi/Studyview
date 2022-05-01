from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFrame, QLineEdit;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;
from gradeplot import GradePlot;
from gradewindow import GradeWindow;
from errorwindow import ErrorWindow;
from addgradewindow import AddGradeWindow;
from grade import Grade;
from time import sleep;
import os, pickle, sys;

appVersion: str = "v1.0";

class MainWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    FontSize: int;
    Font: str;

    GradeList: list;

    App: QApplication;

    # Elements
    AddGradeBtn: QPushButton;
    ShowGradeBtn: QPushButton;
    PlotGradeBtn: QPushButton;
    VersionLbl: QLabel;
    AddGradeLbl: QLabel;
    GradeCountLbl: QLabel;
    AvgGradeLbl: QLabel;
    AddGradeLine: QLineEdit;

    # Subwindows
    ErrWindow: ErrorWindow;
    AddGrdWindow: AddGradeWindow;
    GrdWindow: GradeWindow;
    PlotWindow: GradePlot;
    
    # Init
    def __init__(self, app: QApplication):
        super().__init__();
        self.XSize = 500;
        self.YSize = self.XSize;
        self.Spacing = 60;
        self.FontSize = 14;
        self.Font = "Calibri";
        self.GradeList = [];
        self.App = app;

        self.setFont(QFont(self.Font, self.FontSize));
        self.setWindowTitle("StudyView " + appVersion);
        self.setFixedSize(self.XSize, self.YSize);

        hasGrades: bool = self.getGrades();

        self.AddGradeBtn = QPushButton("ADD GRADE", self);
        width: int = int(self.AddGradeBtn.width() * self.FontSize / 10);
        halfHeight: int = int(self.AddGradeBtn.height()/2);
        self.AddGradeBtn.move(self.XSize - width, int(self.YSize/3) - halfHeight);
        self.AddGradeBtn.clicked.connect(self.addGrade);

        self.ShowGradeBtn = QPushButton("SHOW GRADES", self);
        halfHeight = int(self.ShowGradeBtn.height()/2);
        self.ShowGradeBtn.move(self.XSize - width, int(self.YSize/2) - halfHeight + self.Spacing);
        self.ShowGradeBtn.clicked.connect(self.showGrades);

        self.PlotGradeBtn = QPushButton("PLOT GRADES", self);
        halfHeight = int(self.PlotGradeBtn.height()/2);
        self.PlotGradeBtn.move(self.XSize - width, int(self.YSize/2) - halfHeight + self.Spacing * 2);
        self.PlotGradeBtn.clicked.connect(self.plotData);

        self.VersionLbl = QLabel(self);
        self.VersionLbl.setText("StudyView " + appVersion);
        self.VersionLbl.setFont(QFont(self.Font, 18, 1, True));
        halfWidth = int(self.VersionLbl.width()/2);
        halfHeight = int(self.VersionLbl.height()/2);
        self.VersionLbl.move(int(self.XSize/2) - int(halfWidth * 1.5), self.Spacing);

        self.AddGradeLbl = QLabel(self);
        self.AddGradeLbl.setText("Module name: ");
        halfWidth = int(self.AddGradeLbl.width()/2);
        halfHeight = int(self.AddGradeLbl.height()/2);
        self.AddGradeLbl.move(int(self.Spacing/3), int(self.YSize/3) - halfHeight);

        self.GradeCountLbl = QLabel(self);
        self.GradeCountLbl.setText("No. of grades: " + "None");
        if(hasGrades):
            boldFont = QFont(self.Font, self.FontSize);
            boldFont.setBold(True);
            self.GradeCountLbl.setFont(boldFont);
            self.GradeCountLbl.setText("No. of grades: " + self.loadGradeCount());
        self.GradeCountLbl.move(int(self.Spacing/3), int(self.YSize/2) - halfHeight + self.Spacing);

        self.AvgGradeLbl = QLabel(self);
        self.AvgGradeLbl.setText("Average grade: " + "None");
        if(hasGrades):
            boldFont = QFont(self.Font, self.FontSize);
            boldFont.setBold(True);
            self.AvgGradeLbl.setFont(boldFont);
            self.AvgGradeLbl.setText("Average grade: " + self.loadAvgGrade());
        self.AvgGradeLbl.move(int(self.Spacing/3), int(self.YSize/2) - halfHeight + self.Spacing * 2);

        self.AddGradeLine = QLineEdit(self);
        self.AddGradeLine.setPlaceholderText("Type name here...");
        currWidth = self.AddGradeLine.width();
        self.AddGradeLine.setFixedWidth(currWidth + int(self.Spacing * 1.75));
        halfWidth = int(self.AddGradeLine.width()/2);
        halfHeight = int(self.AddGradeLine.height()/2);
        self.AddGradeLine.move(int(self.Spacing/3) * 2 + self.AddGradeLbl.width(), int(self.YSize/3) - halfHeight);

        self.show();
    
    # Adding grades to storage
    def addGrade(self):
        if(self.AddGradeLine.text() == ""):
            self.ErrWindow = ErrorWindow("NoInput", self.Font, self.FontSize, self.Spacing);
            return;
        else:
            moduleToAdd: str = self.AddGradeLine.text();
            self.AddGrdWindow = AddGradeWindow(moduleToAdd, self.Spacing);
            self.AddGrdWindow.updateSignal.connect(self.gradeUpdate);
    
    def showGrades(self):
        self.GrdWindow = GradeWindow(self.Font, self.FontSize, self.Spacing);

    def getGrades(self) -> bool:
        self.GradeList = [];
        cwd: str = os.getcwd();
        usrData: str = cwd + "\\userdata\\";
        if(not os.path.exists(usrData)):
            os.mkdir(usrData);
        allFiles: list = os.listdir(usrData);
        
        if(allFiles != []):
            fileName: str;
            for fileName in allFiles:
                currFile: str = usrData + fileName;
                with open(currFile, "rb") as f:
                    currGrade: Grade = pickle.load(f);
                    self.GradeList.append(currGrade);
        else:
            return False;
        
        return True;

    # Get no. of grades
    def loadGradeCount(self) -> str:
        gradeCount: int = len(self.GradeList);
        return str(gradeCount);

    # Get average grade
    def loadAvgGrade(self) -> str:
        gradeSum: float = 0;
        divisor: int = int(self.loadGradeCount());
        grade: Grade;

        # Calculation of average grade
        for grade in self.GradeList:
            gradeSum += grade.Grade;
        avgGrade: float = gradeSum/divisor;
        avgGrade = round(avgGrade, 2);

        return str(avgGrade);
    
    # Update grades on AddGrdWindow close
    def gradeUpdate(self):
        plchld0: bool = self.getGrades();
        boldFont = QFont(self.Font, self.FontSize);
        boldFont.setBold(True);
        self.GradeCountLbl.setFont(boldFont);
        self.GradeCountLbl.setText("No. of grades: " + self.loadGradeCount());
        self.AvgGradeLbl.setFont(boldFont);
        self.AvgGradeLbl.setText("Average grade: " + self.loadAvgGrade());
    
    # Plot grade data
    def plotData(self):
        self.PlotWindow = GradePlot(self.GradeList);