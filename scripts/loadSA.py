import os
import sys

sys.path.append(os.getcwd()+'/')

from capstone.models import SubjectArea
import pandas as pd


def run():
    df = pd.read_csv("scripts/subjectarea.csv")
    if len(df) != len(df["subjectID"].unique()):
        print("Data CSV specified has duplicate persNo. Quitting.")
        return
    print("Beginning!")
    ## Loop and save into DB
    for i in df.index:
        if i % 50 == 0:
            print("Currently uploading subject areas {}".format(i))
        subjectArea = SubjectArea()
        subjectArea.subjectID = int(df["subjectID"][i])
        subjectArea.subjectName = df["subjectArea"][i]
        subjectArea.department = df["department"][i]
        subjectArea.faculty = df["faculty"][i]
        subjectArea.save()
    print("Completed! - Loaded {} subject areas to db".format(len(df)))

if __name__ == '__main__':
    run()