import os
import sys

sys.path.append(os.getcwd()+'/')

from capstone.models import Publication
from capstone.models import Researcher

import pandas as pd


def run():
    df = pd.read_csv("scripts/dummypub.csv")

    print("Beginning!")

    ## Loop and save into DB
    for i in df.index:
        if i % 50 == 0:
            print("Currently uploading publications: {}".format(i))

        pubid = int(df['pubID'][i])
        print(pubid)

        if Publication.objects.filter(pubID=pubid).exists():
            publication = Publication.objects.filter(pubID=pubid)[0]
            persno = int(df['persNo'][i])
            researcher = Researcher.objects.get(persNo=persno)
            publication.researchers.add(researcher)
            publication.save()
        else:
            publication = Publication()
            publication.pubID = pubid
            publication.title = df['title'][i]
            publication.numberOfCitations = df['citedby'][i]
            publication.year = df['year'][i]
            publication.save()
            persno = int(df['persNo'][i])
            researcher = Researcher.objects.get(persNo=persno)
            publication.researchers.add(researcher)
            publication.save()
    print("Completed! - Loaded {} publications to db".format(len(df)))

if __name__ == '__main__':
    run()