import os
import json
from .progressBar import ProgressBar

# A class with all kinds of sorts


class FileSort:
    def __init__(self):
        '''Initialises the important parameters required to sort the files.'''
        file_path = os.path.dirname(os.path.abspath(__file__))
        constants_file_path = os.path.join(file_path, "constants.json")
        with open(constants_file_path, "r") as data:
            data = json.load(data)['EXTENSIONS']
            self.EXTENSIONS = data['BASIC_SORT']
            self.ALL_FOLDERS_CREATED = data['ALL_FOLDERS_CREATED']

            self.PATH = os.getcwd()
            self.files_in_directory = os.listdir()
            self.ALL_FOLDERS_CREATED = list(
                map(lambda x: f"{self.PATH}/{x}", self.ALL_FOLDERS_CREATED))

    def createDirectory(self, folderName: str, file: str):
        '''A function to create directories if not created yet and add it to the list of directories. This function
        also moves the files to its respective directory after creating the directory if it doesn't already exist'''

        if folderName not in self.files_in_directory:
            os.mkdir(f"{self.PATH}/{folderName}")
            self.files_in_directory.append(f"{folderName}")

        os.rename(f"{self.PATH}/{file}", f"{self.PATH}/{folderName}/{file}")

    def basic_sort(self, desc=''):
        '''Basic sorting, sorts the files into documents, photos, audiovideo, codingfiles, folders and others based
        on the extensions of the files.'''

        for file in self.files_in_directory:
            root, ext = os.path.splitext(f"{self.PATH}/{file}")

            if ext == '':
                if root in self.ALL_FOLDERS_CREATED:
                    continue
                else:
                    self.createDirectory(folderName="Folders", file=file)

            else:
                self.createDirectory(
                    folderName=self.EXTENSIONS[ext], file=file)

        # Creates a progress bar using the class object ProgressBar and prints the final statement after sorting it.
        pgBar = ProgressBar(desc=desc)
        pgBar.createProgressBar()
        print("Your files have been sorted!")

    def deep_sort(self, desc=''):
        '''This function does deep sorting. It calls the basic sorting algorithm and then continues to deep sort the documents
        based on the extensions into PDF files, word files, ppt files, spreadsheet files, zip files and otehr files'''

        self.basic_sort(desc=desc)
        self.PATH = self.PATH + "/Documents"  # Adding documents to the path.
        # Getting the directories in the documents directory that was created in basic sort
        self.files_in_directory = os.listdir(self.PATH)
        for file in self.files_in_directory:
            _, ext = os.path.splitext(f"{self.PATH}/{file}")

            # Creates folders and sorts the files into these.
            if ext == '':
                continue

            elif ext == '.pdf':
                self.createDirectory(folderName="PDF_FILES", file=file)

            elif ext in ['.docx', '.pages']:
                self.createDirectory(folderName="WORD_FILES", file=file)

            elif ext[0:len(ext)-1] == '.ppt':
                self.createDirectory(folderName="PRESENTATIONS", file=file)

            elif ext[0:len(ext)-1] == '.xls':
                self.createDirectory(folderName="SPREADSHEETS", file=file)

            elif ext == '.zip':
                self.createDirectory(folderName="ZIP_FILES", file=file)

            else:
                self.createDirectory(folderName="OTHER_FILES", file=file)
