# Rename Multi-File

A simple Python script to rename all files in a specified directory that contain a specific string. This script allows users to input the directory, the string to be replaced, and the new string. The script then renames all matching files accordingly.

## Features

- Rename all files containing a specific string in their filename.
- Easy-to-use graphical user interface (GUI) built with `tkinter`.
- Error handling and success messages to guide the user.

## Requirements

- Python 3.6 or later
- `tkinter` (usually included with Python)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/LoneNerd/rename-multi-file.git
```

2. Navigate to the project directory:

```sh
cd rename-multi-file
```

3. Install the required dependencies (if any):

```sh
pip install -r requirements.txt
```

## Usage

1. Run the script:

```sh
python rename_files_gui.py
```

2. Enter the required details in the GUI:
   - Directory path where the files are located.
   - String to be replaced.
   - New string to replace the old string.

3. Click on the "Rename" button to rename the files.

## Building an Executable

To build an executable file from the Python script:

1. Ensure you have `PyInstaller` installed:

```sh
pip install pyinstaller
```

2. Run the following command to create an executable:

```sh
pyinstaller --onefile --windowed rename_files_gui.py
```

3. The executable file will be created in the `dist` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improving this script, feel free to create an issue or submit a pull request. Contributions are always welcome!

---

### Author

**LoneNerd**

GitHub: [LoneNerd](https://github.com/LoneNerd)

```

If you have any more changes or additions you'd like to make, just let me know! 😊🚀
