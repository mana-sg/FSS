import os
import json
from progressBar import ProgressBar


class FileSort:
    def __init__(self):
        with open("extensions.json", "r") as data:
            data = json.load(data)['EXTENSIONS']
            self.IMAGE_EXT = data['IMAGE_EXT']
            self.AV_EXT = data["AV_EXT"]
            self.DOCUMENT_EXT = data['DOCUMENT_EXT']
            self.CODING_EXT = data['CODING_EXT']
            self.ALL_FOLDERS_CREATED = data['ALL_FOLDERS_CREATED']

            self.PATH = os.getcwd()
            self.files_in_directory = os.listdir()
            self.ALL_FOLDERS_CREATED = list(
                map(lambda x: f"{self.PATH}/{x}", self.ALL_FOLDERS_CREATED))

    def createDirectory(self, folderName: str, file: str):
        if folderName not in self.files_in_directory:
            os.mkdir(f"{self.PATH}/{folderName}")
            self.files_in_directory.append(f"{folderName}")

        os.rename(f"{self.PATH}/{file}", f"{self.PATH}/{folderName}/{file}")

    def basic_sort(self, desc=''):
        for file in self.files_in_directory:
            root, ext = os.path.splitext(f"{self.PATH}/{file}")

            if root in self.ALL_FOLDERS_CREATED and ext == '':
                continue

            elif ext in self.IMAGE_EXT:
                self.createDirectory(folderName="Photos", file=file)

            elif ext in self.DOCUMENT_EXT:
                self.createDirectory(folderName="Documents", file=file)

            elif ext in self.AV_EXT:
                self.createDirectory(folderName="AudioVideo", file=file)

            elif ext in self.CODING_EXT and root != f"{self.PATH}/main":
                self.createDirectory(folderName="CodingFiles", file=file)

            elif ext == '' and root not in self.ALL_FOLDERS_CREATED:
                self.createDirectory(folderName="Folders", file=file)

            else:
                self.createDirectory(folderName="Others", file=file)

        pgBar = ProgressBar(desc=desc)
        pgBar.createProgressBar()
        print("Your files have been sorted!")

    def deep_sort(self, desc=''):
        self.basic_sort(desc=desc)
        self.PATH = self.PATH + "/Documents"
        self.files_in_directory = os.listdir(self.PATH)
        for file in self.files_in_directory:
            root, ext = os.path.splitext(f"{self.PATH}/{file}")

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
