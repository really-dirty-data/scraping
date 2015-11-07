import os
import fnmatch

for dirpath, dirnames, filenames in os.walk("."):
     for f in filenames:
         if f.endswith('.dat'):
             print f, dirpath
             os.rename(os.path.join(dirpath, f), os.path.join(dirpath, f.lower()))
         if f.endswith('.DAT'):
             print f, dirpath
             os.rename(os.path.join(dirpath, f), os.path.join(dirpath, f.lower()))
