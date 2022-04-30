import datetime;


# Class to store grade values in
class Grade:
    # Properties
    ModuleName: str;
    Grade: float;
    GradeDate: datetime;
    CP: int;

    # Init
    def __init__(self, modulename: str, grade: float, cp: int, date: datetime.date):
        self.ModuleName = modulename;
        self.Grade = grade;
        self.CP = cp;
        self.GradeDate = date;