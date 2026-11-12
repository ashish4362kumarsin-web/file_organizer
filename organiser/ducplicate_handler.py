from pathlib import Path
import hashlib


class DuplicateHandler:

    def calculateHash(self, filePath):
        sha256 = hashlib.sha256()

        with open(filePath, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    def checkDuplicate(self, source, destination):
        source = Path(source)
        destination = Path(destination)

        if not destination.exists():
            return "NEW"

        sourceHash = self.calculateHash(source)
        destinationHash = self.calculateHash(destination)

        if sourceHash == destinationHash:
            return "DUPLICATE"

        return "DIFFERENT"

    def renameDuplicate(self, destination):
        destination = Path(destination)
        counter = 1

        while True:
            newName = f"{destination.stem} ({counter}){destination.suffix}"
            newPath = destination.with_name(newName)

            if not newPath.exists():
                return newPath

            counter += 1