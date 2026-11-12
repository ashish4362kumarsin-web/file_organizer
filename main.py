from pathlib import Path
import hashlib
import time as t
from organiser.scanner import Scanner
from organiser.classifier import Classifier
from rich.progress import track
from organiser.mover import Mover
from rich.panel import Panel
from rich.align import Align
from rich.console import Group
from rich import print


class FileOrganizer:

    def __init__(self):
        pass

    def UserEntrance(self):
        content = Group(
            Align.center("[bold cyan]Welcome to File Organizer[/bold cyan]"),
            Align.center("[dim]By TeaCoders[/dim]")
        )
        print(
            Panel(
                content,
                border_style="cyan",
                expand=True,
                padding=(1, 0)
            )
        )

        print("We help you to solve the problem of file management!")
        print()
        self.pathManage()
        print()
        print("Process Completed Successfully!")
        
        
    def pathManage(self):
        userFolderPath = input(r"Copy/Paste your folder path: ")  # User folder path input

        self.userFolderPath = Path(userFolderPath).resolve()
        self.scannerData()
        self.classify()
        self.MoverFile()

    def MoverFile(self):
        fileMover = Mover(self.classifiedConfigPath)

        for item in track(range(100), description="Moving files....."):
            t.sleep(0.05)

        movedData = fileMover.checkDestination()

    def scannerData(self):
        # Generate SHA-256 hash --encoding
        userPathString = str(self.userFolderPath)
        hashEncode = hashlib.sha256(userPathString.encode())
        configHash = hashEncode.hexdigest()
        
        #Generate configFile name
        self.concatUserPath = self.userFolderPath.name  #part 1
        self.concatConfigHash = configHash[:6]    # part 2
        self.userconfigFolderName = f"{self.concatUserPath}"  # userconfigFoldername
        
        self.configFolderPath = Path(__file__).resolve().parent / "config"

        self.configFileName = f"{self.concatUserPath}_{self.concatConfigHash}.json"
        self.userconfigFolderName = self.concatUserPath
        self.userconfigFolderPath = self.configFolderPath / self.userconfigFolderName
        self.userconfigFilePath = self.userconfigFolderPath / self.configFileName


        if not self.userconfigFolderPath.exists():
            self.userconfigFolderPath.mkdir(parents=True, exist_ok=True)

        for item in track(range(100), description="Scanning files..."):
            t.sleep(0.06)

        fileScanner = Scanner(  #Scanner.py arguments input
            self.userFolderPath, 
            self.userconfigFolderPath, 
            self.userconfigFilePath)
        
        self.scannedData = fileScanner.UserFiles()

    def classify(self):
        self.classifiedConfigPath = self.userconfigFolderPath / f"{self.concatUserPath}-filtered.json"

        fileClassifier = Classifier(
            self.userFolderPath,
            self.userconfigFilePath,
            self.classifiedConfigPath
        )

        for item in track(range(100), description="Creating Folders..."):
            t.sleep(0.03)

        self.filteredData = fileClassifier.edituserConfig()

        if not self.classifiedConfigPath.exists():
            raise FileNotFoundError(
                f"Classified configuration not created: {self.classifiedConfigPath}"
            )
        
    
if __name__ == '__main__':
    app = FileOrganizer()
    app.UserEntrance()
   