from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QFrame, QLineEdit;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;
from gradeplot import GradePlot;
from gradewindow import GradeWindow;

appVersion: str = "v1.0";

class MainWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;

    # Elements
    AddGradeBtn: QPushButton;
    ShowGradeBtn: QPushButton;
    PlotGradeBtn: QPushButton;
    VersionLbl: QLabel;
    AddGradeLbl: QLabel;
    GradeCountLbl: QLabel;
    AvgGradeLbl: QLabel;
    AddGradeLine: QLineEdit;
    
    # Init
    def __init__(self):
        super().__init__();
        self.XSize = 500;
        self.YSize = self.XSize;
        self.Spacing = 60;
        self.FontSize = 14;
        self.setFont(QFont("Calibri", self.FontSize));
        self.setWindowTitle("StudyView " + appVersion);
        self.setFixedSize(self.XSize, self.YSize);

        self.AddGradeBtn = QPushButton("ADD GRADE", self);
        width: int = int(self.AddGradeBtn.width() * self.FontSize / 10);
        halfHeight: int = int(self.AddGradeBtn.height()/2);
        self.AddGradeBtn.move(self.XSize - width, int(self.YSize/3) - halfHeight);

        self.ShowGradeBtn = QPushButton("SHOW GRADES", self);
        halfHeight = int(self.ShowGradeBtn.height()/2);
        self.ShowGradeBtn.move(self.XSize - width, int(self.YSize/2) - halfHeight + self.Spacing);

        self.PlotGradeBtn = QPushButton("PLOT GRADES", self);
        halfHeight = int(self.PlotGradeBtn.height()/2);
        self.PlotGradeBtn.move(self.XSize - width, int(self.YSize/2) - halfHeight + self.Spacing * 2);

        self.VersionLbl = QLabel(self);
        self.VersionLbl.setText("StudyView " + appVersion);
        self.VersionLbl.setFont(QFont("Calibri", 18, 1, True));
        halfWidth = int(self.VersionLbl.width()/2);
        halfHeight = int(self.VersionLbl.height()/2);
        self.VersionLbl.move(int(self.XSize/2) - int(halfWidth * 1.5), self.Spacing);

        self.AddGradeLbl = QLabel(self);
        self.AddGradeLbl.setText("Module name: ");
        halfWidth = int(self.AddGradeLbl.width()/2);
        halfHeight = int(self.AddGradeLbl.height()/2);
        self.AddGradeLbl.move(int(self.Spacing/3), int(self.YSize/3) - halfHeight);

        self.GradeCountLbl = QLabel(self);
        self.GradeCountLbl.setText("No. of grades: " + "Placeholder");
        # self.GradeCountLbl.setText("No. of grades: " + self.loadGradeCount());
        self.GradeCountLbl.move(int(self.Spacing/3), int(self.YSize/2) - halfHeight + self.Spacing);

        self.AvgGradeLbl = QLabel(self);
        self.AvgGradeLbl.setText("Average grade: " + "Placeholder");
        # self.AvgGradeLbl.setText("Average grade: " + self.loadAvgGrade());
        self.AvgGradeLbl.move(int(self.Spacing/3), int(self.YSize/2) - halfHeight + self.Spacing * 2);

        self.AddGradeLine = QLineEdit(self);
        self.AddGradeLine.setPlaceholderText("Type name here...");
        currWidth = self.AddGradeLine.width();
        self.AddGradeLine.setFixedWidth(currWidth + int(self.Spacing * 1.75));
        halfWidth = int(self.AddGradeLine.width()/2);
        halfHeight = int(self.AddGradeLine.height()/2);
        self.AddGradeLine.move(int(self.Spacing/3) * 2 + self.AddGradeLbl.width(), int(self.YSize/3) - halfHeight);

        self.show();
    
    # def loadGradeCount():
    #     gradeCount: int;
    #     return str(gradeCount);

    # def loadAvgGrade():
    #     avgGrade: int;
    #     return str(avgGrade);
