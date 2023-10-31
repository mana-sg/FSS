from tqdm import tqdm
from time import sleep


class ProgressBar:
    def __init__(self, desc):
        self.desc = desc

    def createProgressBar(self):
        from tqdm import tqdm
        for _ in tqdm(range(100), desc=self.desc):
            sleep(.01)
