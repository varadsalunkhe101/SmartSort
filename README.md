# SmartSort - Automated File Organizer Using Python

## Overview
SmartSort is a Python-based file organization tool that automatically sorts files into folders based on their file extensions. The project helps users keep directories such as Downloads, Desktop, and Documents organized by reducing manual file management.

## Features
* Automatically scans a selected folder
* Detects file types using file extensions
* Creates category folders automatically
* Organizes files into appropriate folders
* Handles unknown file types using an "Others" category
* Displays a summary of moved files

## Categories Supported

| Category  | File Extensions                 |
| --------- | ------------------------------- |
| Images    | .jpg, .jpeg, .png, .gif         |
| Documents | .pdf, .docx, .txt, .pptx, .xlsx |
| Audio     | .mp3, .wav                      |
| Videos    | .mp4, .avi, .mkv                |
| Archives  | .zip, .rar                      |
| Others    | Any unsupported file type       |

## Technologies Used

### Python
The primary programming language used for developing the project.

### OS Module
Used for interacting with the operating system and managing directories.
Functions Used:
* os.listdir()
* os.path.join()
* os.path.exists()
* os.path.isdir()
* os.mkdir()

### Shutil Module
Used for performing high-level file operations.
Function Used:
* shutil.move()

## Project Workflow
1. User specifies the folder path.
2. Program reads all files from the selected folder.
3. File extensions are extracted.
4. Extensions are matched with predefined categories.
5. Category folders are created if they do not exist.
6. Files are moved into their respective folders.
7. A summary report is displayed.

## Example
### Before
Downloads/
* photo.jpg
* resume.pdf
* song.mp3
* movie.mp4
* project.zip

### After
Downloads/
* Images/
* Documents/
* Audio/
* Videos/
* Archives/

## Skills Demonstrated
* Python Programming
* File Handling
* Automation
* Directory Management
* Problem Solving
* Operating System Interaction

## Author
Varad Salunkhe
Computer Science Engineering Student
