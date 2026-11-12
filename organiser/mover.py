import json
from pathlib import Path
import shutil
from organiser.ducplicate_handler import DuplicateHandler

class Mover:
    def __init__(self, classifiedConfigFilePath):
        self.classifiedConfigFilePath = Path(f"{classifiedConfigFilePath}")
        self.duplicateHandler = DuplicateHandler()

    def loadClassifiedConfig(self):
        if not self.classifiedConfigFilePath.exists():
            raise FileNotFoundError(
                f"Classified JSON file not found: "
                f"{self.classifiedConfigFilePath}"
            )
        
        with open(self.classifiedConfigFilePath, "r") as file:
            loadData = json.load(file)

        return loadData

    def checkDestination(self):
        fileConfig = self.loadClassifiedConfig()

        for filename, details in fileConfig.items():
            source = Path(details["SourcePath"])
            destination = Path(details["DestinationPath"]) / filename

            if not source.is_file():
                print(f"Source file does not exist: {source}")
                continue

            try:
                result = self.duplicateHandler.checkDuplicate(source, destination)

                if result == "NEW":
                    pass

                elif result == "DUPLICATE":
                    print(f"Duplicate file skipped: {filename}")
                    continue

                elif result == "DIFFERENT":
                    destination = self.duplicateHandler.renameDuplicate(destination)

                destination.parent.mkdir(parents=True, exist_ok=True)

                self.moveFile(source, destination)

            except OSError as e:
                print(f"Destination error: {e}")

    def moveFile(self, source: Path, destination: Path):
        # Using shutil --Moving files
        
        try:
            shutil.move(str(source), str(destination))

        except (shutil.Error, OSError) as e:
           print(f"Failed to move {source.name}: {e}")