import os

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



def Main():
    pytex_files = GetPyTeXList()
    GetPyTeXSelections(pytex_files)

Main()
