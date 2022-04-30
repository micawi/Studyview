from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt, pyqtSignal;
from gradeaddedmsg import GradeAddedMsg;
from errorwindow import ErrorWindow;
from grade import Grade;
import os, pickle, datetime;

class AddGradeWindow(QWidget):
    # Properties
    XSize: int;
    YSize: int;
    Spacing: int;
    FontSize: int;
    Font: str;

    # Signal
    updateSignal = pyqtSignal();

    # Elements
    ModuleLbl: QLabel;
    GradeLine: QLineEdit;
    CPLbl: QLabel;
    CPLine: QLineEdit;
    AddGrdBtn: QPushButton;
    CancelBtn: QPushButton;
    DateLbl: QLabel;
    DateLine: QLineEdit;
    TodayLbl : QLabel;
    TodayCheck: QCheckBox;

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

        self.DateLbl = QLabel(self);
        self.DateLbl.setText("Date: ");
        self.DateLbl.move(int(self.Spacing/2), int(self.Spacing));

        self.DateLine = QLineEdit(self);
        self.DateLine.setPlaceholderText("dd.mm.yy");
        self.DateLine.setEnabled(False);
        self.DateLine.setMaxLength(8);
        self.DateLine.setFixedWidth(int(self.Spacing * 1.5));
        self.DateLine.move(int(self.Spacing * 1.05), int(self.Spacing));

        self.TodayLbl = QLabel(self);
        self.TodayLbl.setText("Today: ");
        self.TodayLbl.move(int(self.Spacing * 3), int(self.Spacing));

        self.TodayCheck = QCheckBox(self);
        self.TodayCheck.setChecked(True);
        self.TodayCheck.move(int(self.Spacing/2) + int(width * 1.9), int(self.Spacing));
        self.TodayCheck.toggled.connect(self.dateCheck);

        self.AddGrdBtn = QPushButton("ADD GRADE", self);
        self.AddGrdBtn.move(int(self.Spacing/2), self.Spacing * 2);
        self.AddGrdBtn.setFixedWidth(self.XSize - self.Spacing);
        self.AddGrdBtn.clicked.connect(self.addGrade);

        self.CancelBtn = QPushButton("CANCEL", self);
        width = self.CancelBtn.width();
        self.CancelBtn.move(int(self.XSize/2) - int(width/2.75), int(self.Spacing * 2.5));
        self.CancelBtn.clicked.connect(self.cancel);

        self.show();
    
    # Make dateline editable/uneditable
    def dateCheck(self):
        if(self.TodayCheck.isChecked()):
            self.DateLine.setText("");
            self.DateLine.setEnabled(False);
        else:
            self.DateLine.setEnabled(True);                
    
    # Adding of grade to specified file/location
    def addGrade(self):
        gradeName: str = self.ModuleLbl.text();
        gradeName = gradeName.replace(": ", "");
        gradeStr: str = self.GradeLine.text();
        cpStr: str = self.CPLine.text();

        if((gradeStr != "") & (cpStr != "")):
            try:
                grade: float = float(gradeStr);
                cp: int = int(cpStr);
                if(not self.TodayCheck.isChecked()):
                    dateText: str = self.DateLine.text().replace(".", "/");
                    date: datetime.date = datetime.datetime.strptime(dateText, "%d/%m/%y");
                else:
                    date: datetime = datetime.date.today();
            except:
                self.ErrWindow = ErrorWindow("WrongInput", self.Font, 14, self.Spacing);
                return;
            cwd: str = os.getcwd();
            usrData: str = cwd + "/userdata/";
            gradePath: str = usrData + gradeName + ".dat";

            if(not os.path.exists(usrData)):
                os.mkdir(usrData);
            
            if(not os.path.exists(gradePath)):
                with open(gradePath, "wb") as f:
                    grade = Grade(gradeName, grade, cp, date);
                    pickle.dump(grade, f);
            else:
                self.ErrWindow = ErrorWindow("ModuleExists", self.Font, 14, self.Spacing);
                return;
        else:
            self.ErrWindow = ErrorWindow("Empty", self.Font, 14, self.Spacing);
            return;

        self.GrdAddedMsg = GradeAddedMsg(self.Spacing);
        self.close();
    
    def closeEvent(self, event):
        self.updateSignal.emit();

    
    # Close on cancel
    def cancel(self):
        self.close();
