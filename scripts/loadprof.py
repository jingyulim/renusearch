import os
import sys

sys.path.append(os.getcwd()+'/')

from capstone.models import Researcher
import pandas as pd


def run():
    df = pd.read_csv("scripts/dummyprof.csv")
    if len(df) != len(df["persNo"].unique()):
        print("Data CSV specified has duplicate persNo. Quitting.")
        return
    print("Beginning!")
    ## Loop and save into DB
    for i in df.index:
        if i % 50 == 0:
            print("Currently uploading professor {}".format(i))
        researcher = Researcher()
        researcher.persNo = int(df["persNo"][i])
        researcher.firstName = df["firstName"][i]
        researcher.lastName = df["lastName"][i]
        researcher.name = df["name"][i]
        researcher.department = df["department"][i]
        researcher.faculty = df["faculty"][i]
        researcher.position = df["position"][i]
        researcher.numberOfPubs = df["numPubs"][i]
        researcher.numberOfCitations = df["numCitations"][i]
        researcher.hIndex = df["hIndex"][i]
        researcher.save()
    print("Completed! - Loaded {} professors to db".format(len(df)))

if __name__ == '__main__':
    run()
