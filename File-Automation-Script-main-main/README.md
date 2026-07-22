# File Automation Script

## Project Overview

This project is a Python-based file automation tool that helps organize files and perform basic file management tasks automatically.

The script can:

- Sort files into folders based on file type
- Rename files in bulk
- Delete empty folders
- Generate logs for all operations
- Handle errors using exception handling

## Technologies Used

- Python
- os module
- shutil module
- logging module

## Features

### 1. Sort Files

Files are automatically moved into folders such as:

- Images
- Documents
- Audio
- Videos
- Others

### 2. Rename Files

Files inside a folder can be renamed using a custom prefix.

Example:

Before:

```text
report.pdf
notes.txt
```

After:

```text
project_1.pdf
project_2.txt
```

### 3. Delete Empty Folders

The script scans the selected directory and removes folders that do not contain any files.

### 4. Logging

All operations are recorded in `automation.log`.

Example:

```text
2026-06-25 18:00:10 - INFO - moved report.pdf to Documents
```

## Project Structure

```text
File-Automation-Script/
│
├── automation.py
├── README.md
├── automation.log
└── sample_test_folder/
```

## How to Run

1. Open the project folder in VS Code.
2. Open Terminal.
3. Run:

```bash
python automation.py
```

4. Choose an option from the menu.

## Menu Options

```text
1. Sort files
2. Rename files
3. Delete empty folders
4. Exit
```

## Sample Input

```text
Enter choice: 1
Enter path: C:\Users\User\Desktop\sample_test_folder
```

## Sample Output

```text
moved: photo.jpg
moved: report.pdf
moved: song.mp3
```

## Learning Outcomes

Through this project, I learned:

- Working with files and folders using Python
- Using the os module
- Exception handling
- Logging operations
- Creating automation scripts
- Using Git and GitHub for version control

## Author

S Mahammad Nadhim 
