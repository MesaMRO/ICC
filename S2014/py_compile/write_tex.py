import os
import re
import sys
from datetime import date
from datetime import time

# Get list of all pytex files
def GetPyTeXList():
    pytex_files = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.pytex'):
                pytex_files.append(os.path.join(root,f))
    return pytex_files

# Get selections from list of files
def GetPyTeXSelections(files):
    if not files:
        print('Error: No PyTeX documents in directory tree.')
    else:
        for i in range(0, len(files)):
            print('[%s]: "%s"'%(i, files[i]))

def OpenTexFile():
    texfile_name = re.sub('\.py','',__file__)+'.tex'
    texfile = open(texfile_name, 'w')
    return texfile

def WriteTexFile():
    texfile = OpenTexFile()
    texfile.close()

def MakePreamble(packages):
    preamble = []
    preamble.append("\documentclass{article}")
    for p in packages:
        preamble.append(p)
    return preamble

# Make title info tuple
def MakeTitle(name, event, date):
    title = (
        "\\begin{center}",
        "{\LARGE\scshape %s}\\[0.2cm]"%name,
        "{\Large\scshape %s}\\[0.2cm]"%event,
        "{\large %s}"%date,
        "\end{center}")
    return title

# packages = [
#     ["babel",["english"]],
#     ["inputenc",["utf8"]],
#     ["fontenc",["T1"]],
#     ["titlesec"],
#     ["tabularx"],
#     ["booktabs"]
# ]

# packagelist = MakePackageEntryList(packages)
# preamble = MakePreamble(packagelist)

# title = MakeTitle(
#     "Mesa Robotics Organization",
#     "Meeting Minutes",
#     meeting_date.strftime("%B %A, %Y"))

# texfile = OpenTexFile()
# texfile.writelines(preamble)
# texfile.writelines(title)
# texfile.close()

##################################################
doc = []

class Member:
    last = None
    first = None
    email = None
    position = None

# Make a single package entry string
def MakePackageEntry(package):
    if not type(package) is tuple:
        return "\\usepackage{%s}"%package
    else:
        s = "\\usepackage"
        for i in range(1,len(package)):
            s += "[%s]"%package[i]
        s += "{%s}"%package[0]
        return s

# Make tuple of package entry strings
def MakePackageEntryList(packages):
    return list(map(MakePackageEntry, packages))

def MakeMember(member):
    if len(member) is 4:
        return 0

# Packages
packages = [
    ("babel","english"),
    ("inputenc","utf8"),
    ("fontenc","T1"),
    "titlesec",
    "tabularx",
    "booktabs"
]

# Meeting info
meeting_date = date(2014, 2, 28)
meeting_start = time(13)
meeting_end = time(14)

for p in MakePackageEntryList(packages):
    print(p)