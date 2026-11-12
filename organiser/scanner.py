
import json
from pathlib import Path


class Scanner:
    def __init__(self, userFolderPath, configFolderPath, configFilePath):
        self.userFolderPath = Path(f"{userFolderPath}")
        self.configFolderPath = Path(f"{configFolderPath}")
        self.configFilePath = Path(f"{configFilePath}")
# Create configuration file
    def ConfigFile(self):

        self.configFilePath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.configFilePath.exists() or self.configFilePath.stat().st_size == 0:
            with open(self.configFilePath, "w") as file:
                json.dump({}, file, indent=4)

    # Read existing configuration
    def loadConfig(self):
        self.ConfigFile()

        with open(self.configFilePath, "r") as file:
            return json.load(file)


    # Store current working directory
    def addCurrentPath(self):
        configData = self.loadConfig()
        configData["CurrentPath"] = str(Path.cwd())

        with open(str(self.configFilePath), "w") as file:
            json.dump(configData, file, indent=4)

    # Scan user files
    def UserFiles(self):
        files = {}
        for items in self.userFolderPath.rglob("*"):
            if items.is_file():
                parentFolder = str(items.parent)
                if parentFolder not in files:
                    files[parentFolder] = {}

                files[parentFolder][items.name] = {
                    "Extension": items.suffix,
                    "Name": items.stem,
                    "FullName": items.name,
                    "Path": str(items.resolve())
                }
        # Load existing configuration
        self.configData = self.loadConfig()

        # Update scanned folder information
        self.configData.update(files)

        # Write updated data
        
        with open(str(self.configFilePath), "w") as file:
            json.dump(self.configData, file, indent=4)


        return self.configData




