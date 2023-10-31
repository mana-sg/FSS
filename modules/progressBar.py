from tqdm import tqdm
from time import sleep

# A class to create a terminal based progress bar using tqdm


class ProgressBar:
    def __init__(self, desc):
        '''Initialises the description to be displayed while the progress of the operation.'''
        self.desc = desc

    def createProgressBar(self):
        '''Creates a progress bar in the terminal to depict the progress of the files.'''
        for _ in tqdm(range(100), desc=self.desc):
            sleep(.01)
