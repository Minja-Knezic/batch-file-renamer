# Batch File and Directory Renamer

## Overview
The **Batch File and Directory Renamer** is a Python script designed to streamline the process of renaming multiple files and directories in a specified folder. Users can customize the renaming process by adding prefixes, suffixes, and replacing specific text. This tool is ideal for organizing files, renaming batches of images, or standardizing naming conventions in a directory.

## Features
- **Batch File Renaming**: Add prefixes, suffixes, or replace parts of file names.
- **Directory Renaming**: Optionally rename directories alongside files.
- **Extension Filtering**: Rename only files with a specified extension (e.g., `.txt`, `.jpg`).
- **Interactive Input**: User-friendly prompts for all customization options.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/batch-file-renamer.git
   cd batch-file-renamer
   ```

2. Run the script:
   ```bash
   python batch_renamer.py
   ```

3. Follow the prompts to specify:
   - The directory containing files and/or directories to rename.
   - Prefix or suffix to add to file and directory names.
   - Text to replace and its replacement (optional).
   - File extension to filter (optional).
   - Whether directories should be renamed as well.

## Example
### Input
```
Enter the directory path: ./example
Enter prefix (or leave blank): new_
Enter suffix (or leave blank): _v1
Text to replace (or leave blank): old
Replacement text (or leave blank): new
Filter by file extension (e.g., .txt) or leave blank for all:
Do you want to rename directories as well? (yes/no): yes
```

### Output
- Files:
  - `oldfile.txt` → `new_newfile_v1.txt`
- Directories:
  - `olddir` → `new_newdir_v1`

## Requirements
- Python 3.7 or later

## Installation
- Ensure Python is installed on your system.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for bug fixes or new features.


## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to reach out with feedback or suggestions to improve this tool!

