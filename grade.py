class Grade:
    # Properties
    ModuleName: str;
    Grade: float;
    CP: int;

    # Init
    def __init__(self, modulename: str, grade: float, cp: int):
        self.ModuleName = modulename;
        self.Grade = grade;
        self.CP = cp;