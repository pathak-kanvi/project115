import os

source = 'beforeRename.txt'
destination = 'afterRename.txt'
os.rename(source, destination)
print("Renamed! :)")
