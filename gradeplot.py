import matplotlib.pyplot as plt;
from matplotlib import rc;
from grade import Grade;


class GradePlot:
    # Properties
    XValues1: list;
    XValues2: list;
    YValues1: list;
    YValues2: list;

    # Init
    def __init__(self, gradeList: list):
        self.XValues1 = [];
        self.XValues2 = [];
        self.YValues1 = [];
        self.YValues2 = [];

        font = {"family" : "calibri",
                "weight" : "normal",
                "size" : 10};

        grade: Grade;
        for grade in gradeList:
            self.XValues1.append(grade.GradeDate);
            self.YValues1.append(grade.Grade);
        
        
        currAvg: int;
        counter: int = 1;
        gradeSorted = sorted(gradeList, reverse=False, key=lambda x: x.GradeDate); # Sort grades with date
        for grade in gradeSorted:
            self.XValues2.append(grade.GradeDate);
            if(counter != 1):
                currAvg = (currAvg * (counter - 1) + grade.Grade)/counter; # Calculate new average from old average
            else:
                currAvg = grade.Grade;
            self.YValues2.append(currAvg);
            counter += 1;
        
        plt.plot(self.XValues1, self.YValues1, "rs", self.XValues2, self.YValues2, "b--");
        plt.legend(labels=["Grades", "Total Avg. Grade"], fontsize=8);
        plt.title("Grade plot");
        plt.ylabel("Grade");
        plt.xlabel("Date");
        plt.xticks(**font);
        plt.show();