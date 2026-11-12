# 📁 File Organizer

A Python-based file organization tool that automatically scans, classifies, and organizes files into folders based on their file extensions.

The goal of this project is to make file management easier by reducing manual work and keeping directories clean and organized.

---

## ✨ Features

- **Automatic File Scanning:** Scans the selected directory and collects file information.
- **File Classification:** Identifies file types based on their extensions.
- **Automatic Folder Creation:** Creates folders according to file categories.
- **File Moving:** Moves files into their respective categorized folders.
- **Duplicate Detection:** Detects duplicate files to prevent unnecessary copies.
- **Progress Bar:** Displays real-time progress during file organization.
- **Error Handling:** Handles missing files and other file operation errors.

---

## 🛠️ Technologies Used

| Technology | Purpose                                  |
| ---------- | ---------------------------------------- |
| Python     | Core programming language                |
| pathlib    | File and directory management            |
| os         | Operating system interactions            |
| json       | Configuration and data storage           |
| hashlib    | Duplicate file detection                 |
| Rich       | Terminal progress bars and visual output |

---

## 📂 Project Structure

```text
File_Organizer/
│
├── main.py
│
├── organiser/
│   ├── __init__.py
│   ├── scanner.py
│   ├── classifier.py
│   ├── mover.py
│   └── duplicate_handler.py
│
├── config/
│   └── config.json
│
├── README.md
│
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd File_Organizer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

---

## 🚀 How to Use

1. Run the application.
2. Enter the directory path you want to organize.
3. The application scans the selected directory.
4. Files are classified according to their extensions.
5. Required folders are created automatically.
6. Files are moved into their respective folders.
7. Duplicate files are detected and handled.

---

## 📋 Example

### Before Organization

```text
Downloads/
│
├── photo.jpg
├── document.pdf
├── music.mp3
├── video.mp4
├── program.py
└── notes.txt
```

### After Organization

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   ├── document.pdf
│   └── notes.txt
│
├── Audio/
│   └── music.mp3
│
├── Videos/
│   └── video.mp4
│
└── Coding/
    └── program.py
```

---

## 🔍 Duplicate Detection

The project uses Python's `hashlib` module to calculate file hashes and identify duplicate files.

This helps detect files with identical content, even when their filenames are different.

---

## 🔮 Future Improvements

- [ ] GUI-based interface.
- [ ] Custom file categories.
- [ ] File restoration functionality.
- [ ] Detailed organization reports.
- [ ] Logging system.
- [ ] Support for more file formats.
- [ ] Improved duplicate management.

---

## 🎯 Project Goal

This project is built to improve practical Python programming skills through real-world file management operations, modular programming, error handling, and working with external Python libraries.

---

## 👨‍💻 Author

**Ashish**

A Python programming enthusiast interested in software development and building practical technology solutions.

---

⭐ If you find this project useful, consider giving it a star!
