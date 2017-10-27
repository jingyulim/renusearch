import os
import sys

sys.path.append(os.getcwd()+'/')

from capstone.models import SubjectArea
from capstone.models import Researcher
import pandas as pd

def run():
	researchers = Researcher.objects.all()
	print("BEGIN")
	for r in researchers:
		dept = r.department
		suba = SubjectArea.objects.filter(department=dept)[0]
		r.subjectArea = suba
		r.save()
	print("Completed! - Loaded {} researcher's subject area to db".format(len(researchers)))

if __name__ == '__main__':
    run()