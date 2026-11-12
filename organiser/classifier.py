import json
from pathlib import Path




class Classifier:
    def __init__(self, userFolderPath, userConfigFilePath, classifiedConfigPath):
        self.userFolderPath = Path(f"{userFolderPath}")
        self.userConfigFilePath = Path(f"{userConfigFilePath}")
        self.classifiedConfigPath = Path(f"{classifiedConfigPath}")
        self.codeFolder = self.userFolderPath / "Coding"

    def loaduserConfig(self):
        #loading json Data

        with open(self.userConfigFilePath, "r") as file:
            self.userData = json.load(file)

        return self.userData


    def edituserConfig(self):
        checkuserData = self.loaduserConfig()
        addConfigData = {}

        for folderPath, files in checkuserData.items():
            for filename, details in files.items():

                extension = details["Extension"].lower()
                path = details["Path"]

                destination = self.categoryList(extension)

                addConfigData[filename] = {
                    "Extension": extension,
                    "SourcePath": path,
                    "DestinationPath": str(destination)
                }

        self.classifiedConfigPath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.classifiedConfigPath, "w") as file:
            json.dump(addConfigData, file, indent=4)

        return addConfigData
    def categoryList(self, extension):
        

        # Images
        if extension in {
            ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp",
            ".tiff", ".tif", ".ico", ".heic", ".heif", ".raw", ".cr2",
            ".nef", ".arw", ".dng", ".psd", ".ai", ".eps", ".avif",
            ".jxl", ".jp2", ".exr", ".hdr"
        }:
            destination = self.userFolderPath / "Images"

        # Documents
        elif extension in {
            ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".pages",
            ".md", ".tex", ".wpd", ".wps", ".djvu", ".xps", ".oxps",
            ".epub"
        }:
            destination = self.userFolderPath / "Documents"

        # Spreadsheets
        elif extension in {
            ".xls", ".xlsx", ".csv", ".ods", ".tsv", ".xlsm", ".xlsb",
            ".numbers"
        }:
            destination = self.userFolderPath / "Spreadsheets"

        # Presentations
        elif extension in {
            ".ppt", ".pptx", ".odp", ".key", ".pps", ".ppsx"
        }:
            destination = self.userFolderPath / "Presentation Slides"

        # Videos
        elif extension in {
            ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
            ".m4v", ".3gp", ".mpeg", ".mpg", ".vob", ".ts", ".mts",
            ".m2ts", ".ogv", ".rm", ".rmvb", ".asf", ".divx"
        }:
            destination = self.userFolderPath / "Videos"

        # Audio
        elif extension in {
            ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma",
            ".aiff", ".aif", ".opus", ".mid", ".midi", ".amr", ".ac3",
            ".dts", ".ape", ".alac", ".dsf", ".dff"
        }:
            destination = self.userFolderPath / "Audio"

        # Archives / Compressed
        elif extension in {
            ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
            ".iso", ".cab", ".arj", ".lzh", ".lz", ".lzma", ".zst",
            ".tgz", ".tbz2", ".txz", ".br", ".cpio"
        }:
            destination = self.userFolderPath / "Compressed"

        # Coding - Python
        elif extension in {".py", ".pyc", ".pyo"}:
            destination = self.codeFolder / "Python"

        # Coding - Node
        elif extension in {".js", ".tsx", ".mjs", ".cjs", ".ts"}:
            destination = self.codeFolder / "Node"

        # Coding - HTML and CSS
        elif extension in {
            ".html", ".htm", ".css", ".scss", ".sass", ".less"
        }:
            destination = self.codeFolder / "Html and CSS"

        # Coding - Java
        elif extension in {".jsx", ".java", ".class", ".jar"}:
            destination = self.codeFolder / "Java"

        # Coding - C and C++
        elif extension in {".c", ".cpp", ".h", ".hpp"}:
            destination = self.codeFolder / "C and C++"

        # Coding - C#
        elif extension == ".cs":
            destination = self.codeFolder / "C#"

        # Coding - PHP
        elif extension == ".php":
            destination = self.codeFolder / "PHP"

        # Coding - Ruby
        elif extension == ".rb":
            destination = self.codeFolder / "Ruby"

        # Coding - Go
        elif extension == ".go":
            destination = self.codeFolder / "GOLang"

        # Coding - Rust
        elif extension == ".rs":
            destination = self.codeFolder / "Rust"

        # Coding - Swift
        elif extension == ".swift":
            destination = self.codeFolder / "Swift"

        # Coding - Kotlin
        elif extension in {".kt", ".kts"}:
            destination = self.codeFolder / "Kotlin"

        # Coding - Dart
        elif extension == ".dart":
            destination = self.codeFolder / "Dart"

        # Coding - Lua
        elif extension == ".lua":
            destination = self.codeFolder / "Lua"

        # Coding - Perl
        elif extension == ".pl":
            destination = self.codeFolder / "Perl"

        # Coding - R
        elif extension == ".r":
            destination = self.codeFolder / "R"

        # Coding - Scala
        elif extension == ".scala":
            destination = self.codeFolder / "Scala"

        # Coding - Clojure
        elif extension == ".clj":
            destination = self.codeFolder / "Clojure"

        # Coding - Elixir
        elif extension in {".ex", ".exs"}:
            destination = self.codeFolder / "Elixir"

        # Coding - Erlang
        elif extension in {".erl", ".hrl"}:
            destination = self.codeFolder / "Erlang"

        # Haskell
        elif extension in {".hs", ".lhs"}:
            destination = self.codeFolder / "Haskell"

        # OCaml
        elif extension in {".ml", ".mli"}:
            destination = self.codeFolder / "OCaml"

        # F#
        elif extension in {".fs", ".fsx"}:
            destination = self.codeFolder / "FSharp"

        # SQL
        elif extension == ".sql":
            destination = self.codeFolder / "SQL"

        # JSON
        elif extension in {".json", ".jsonc"}:
            destination = self.codeFolder / "JSON"

        # XML
        elif extension == ".xml":
            destination = self.codeFolder / "XML"

        # YAML
        elif extension in {".yaml", ".yml"}:
            destination = self.codeFolder / "YAML"

        # TOML
        elif extension == ".toml":
            destination = self.codeFolder / "TOML"

        # INI
        elif extension == ".ini":
            destination = self.codeFolder / "INI"

        # GraphQL
        elif extension in {".graphql", ".gql"}:
            destination = self.codeFolder / "GraphQL"

        # Protocol Buffers
        elif extension == ".proto":
            destination = self.codeFolder / "Protocol Buffers"

        # Shell Scripts
        elif extension in {".sh", ".bash", ".zsh"}:
            destination = self.codeFolder / "Shell Scripts"

        # Windows Batch
        elif extension in {".bat", ".cmd"}:
            destination = self.codeFolder / "Windows Batch"

        # PowerShell
        elif extension == ".ps1":
            destination = self.codeFolder / "PowerShell"

        # Docker
        elif extension == ".dockerfile":
            destination = self.codeFolder / "Docker"

        # Makefile
        elif extension == ".makefile":
            destination = self.codeFolder / "Makefile"

        # Gradle
        elif extension == ".gradle":
            destination = self.codeFolder / "Gradle"

        # Applications / Installers
        elif extension in {
            ".exe", ".msi", ".apk", ".appx", ".appxbundle",
            ".deb", ".rpm", ".dmg", ".pkg", ".app", ".ipa",
            ".jar", ".bin", ".run", ".appimage"
        }:
            destination = self.userFolderPath / "Application/Installers"

        # Fonts
        elif extension in {
            ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon",
            ".fnt", ".pfb", ".pfm"
        }:
            destination = self.userFolderPath / "Fonts"

        # 3D / CAD / Design
        elif extension in {
            ".obj", ".stl", ".fbx", ".blend", ".3ds", ".gltf",
            ".glb", ".step", ".stp", ".dwg", ".dxf", ".iges",
            ".igs", ".3mf", ".dae", ".usd", ".usdz", ".abc",
            ".max", ".ma", ".mb", ".skp", ".sldprt", ".sldasm"
        }:
            destination = self.userFolderPath / "3D/CAD"

        # Database
        elif extension in {
            ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",
            ".dbf", ".sqlitedb", ".realm", ".bson"
        }:
            destination = self.userFolderPath / "DataBase"

        # E-books
        elif extension in {
            ".epub", ".mobi", ".azw", ".azw3", ".djvu",
            ".fb2", ".lit", ".pdb", ".cbr", ".cbz"
        }:
            destination = self.userFolderPath / "E-Books"

        # System / Configuration
        elif extension in {
            ".cfg", ".conf", ".log", ".tmp", ".bak", ".dat",
            ".reg", ".sys", ".dll", ".drv", ".ocx", ".so",
            ".dylib", ".ini", ".plist", ".service", ".desktop"
        }:
            destination = self.userFolderPath / "System/Configs"

        # Virtual Machines / Disk Images
        elif extension in {
            ".vdi", ".vmdk", ".vhd", ".vhdx", ".qcow2",
            ".ova", ".ovf", ".vbox", ".vmx"
        }:
            destination = self.userFolderPath / "Virtual Machine"

        # Backup / Data
        elif extension in {
            ".bak", ".old", ".backup", ".dump", ".sql",
            ".parquet", ".avro", ".orc", ".feather", ".arrow"
        }:
            destination = self.userFolderPath / "BackUps"

        # Subtitles
        elif extension in {".srt", ".ass", ".ssa", ".sub", ".vtt", ".sbv"}:
            destination = self.userFolderPath / "SubTitles"

        # Torrents
        elif extension == ".torrent":
            destination = self.userFolderPath / "Torrent"

        # Game Development
        elif extension in {
            ".unity", ".unitypackage", ".uasset", ".umap",
            ".pak", ".wad", ".bsp", ".asset"
        }:
            destination = self.userFolderPath / "Game Development"

        # Others
        elif extension in {
            ".ics", ".vcf", ".eml", ".msg", ".pst", ".ost",
            ".torrent", ".pem", ".crt", ".cer", ".key", ".p12",
            ".pfx"
        }:
            destination = self.userFolderPath / "Others"

        else:
            destination = self.userFolderPath / "Others"

        #Creating folder Accordingly
        destination.mkdir(parents=True, exist_ok=True)

        return destination           

                     
    