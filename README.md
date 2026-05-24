# Python & Bash File Organiser

A file organisation automation project built with Python and Bash scripting. The program automatically scans a folder, detects file types, creates matching directories and moves files into organised categories. The project was created to practise scripting, automation, file handling and basic Linux concepts.

---

## Features

### Python Version
- Organises files by extension
- Automatically creates folders if they do not exist
- Handles unknown file types using an "Other" folder
- Prevents duplicate file overwriting by renaming files
- Logs file movements with timestamps
- Uses dictionaries for extension mapping
- Uses loops and conditionals for automation

### Bash Version
- Uses Bash loops and wildcards to move files
- Creates directories using `mkdir -p`
- Uses `mv` commands for file organisation
- Includes terminal logging with `echo`
- Uses `nullglob` to safely handle missing file matches

---

## Technologies Used

- Python 3
- Bash
- os module
- shutil module
- datetime module
- Linux terminal commands
- Git & GitHub

---

## Example Folder Structure

### Before

```text
test-files/
├── cat.png
├── music.mp3
├── homework.pdf
├── notes.txt
```

### After

```text
test-files/
├── Images/
│   └── cat.png
│
├── Audio/
│   └── music.mp3
│
├── Documents/
│   ├── homework.pdf
│   └── notes.txt
```

---

## What I Learned

This project helped me practise:
- Python and Bash scripting fundamentals
- File system automation and path handling
- Logging and timestamp generation
- Defensive programming and duplicate file handling
- Testing automation scripts safely using dummy files

I also learned the importance of handling edge cases, such as unknown file types and duplicate filenames, to make automation scripts safer and more reliable.

---

## Reflection

This project was one of my first experiences building an automation script that interacts directly with the operating system and file system. Initially, I only understood the basic idea of looping through files, but while developing the organiser I became more confident using dictionaries, conditions, file paths and modules such as `os` and `shutil`.

The most challenging part was handling duplicate filenames safely without overwriting existing files. Implementing a counter system helped me better understand loops, path checking and defensive programming concepts. I also learned why testing on dummy files is important before using automation scripts on real directories.

Creating the Bash version helped reinforce Linux and scripting fundamentals in a simpler and more direct way. Comparing Bash and Python also improved my understanding of how different scripting languages approach automation tasks.

Overall, this project strengthened my understanding of automation, scripting and problem-solving while helping me build confidence working with real file-system operations.

---

## How to Run

### Python Version

1. Place files inside the `test-files` folder
2. Run the script:

```bash
python organiser.py
```

### Bash Version

1. Make the script executable:

```bash
chmod +x organiser.sh
```

2. Run the script:

```bash
./organiser.sh
```

---

## Future Improvements

- Add support for more file types
- Add recursive folder scanning
- Allow custom destination folders
- Add GUI version using Python Tkinter
- Export logs to CSV format
- Add error handling using `try` and `except`