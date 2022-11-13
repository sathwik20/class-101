from distutils import extension
from importlib.resources import path
import os
import shutil

#path='C:/Users/admin/OneDrive/Pictures/102/duck.txt'

#root,extension=os.path.splitext(path)

#print('root of the path: ',root)
#print('extension of the path: ',extension)

source = 'C:/Users/admin/OneDrive/Pictures/102/duck.txt'
destination='C:/Users/admin/OneDrive/Pictures/'
#dest = shutil.copy(source,destination)
dest1 = shutil.move(source,destination)