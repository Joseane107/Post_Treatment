## Good practices in Python: https://peps.python.org/pep-0008/ ##

from pathlib import Path
from glob import glob
import sys
import os

class post_ADF:
    def __init__(self, filename, spin=False):
        self.directory = Path("./files/")
        self.spin = spin
        self.path = None
        self.filename = filename


        #Finding the path for the file
        for x in os.walk(self.directory):
            for y in glob(os.path.join(x[0], f'{filename}')):
                self.path = y

        #Print if the file was found or not
        if self.path is None:
            sys.exit('File not found. Check name and path.')
        else:
            sys.stdout.write(f'The File is here: {self.path}')


'''
        self.path = [y for x in os.walk(self.directory) for y in glob(os.path.join(x[0], f'{filename}'))][0]
        #print(f'{glob(os.path.join(x[0])}')
        if self.path is None:
            sys.exit('Sorry, filename not found. Exiting.')
        else:
            sys.stdout.write(f'The File is here: {self.path}')

'''

