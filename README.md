# Sticky Notes App

This is a simple Sticky Notes application built with Python and Tkinter. It allows users to add, delete, and save notes. The application uses a text file to store the notes, ensuring that they persist between sessions.

## Features
 - Create Notes: Easily add new notes with a click of a button.
 - Manage Notes: Edit existing notes or delete them when no longer needed.
 - Persistent Storage: All notes are automatically saved to a text file (notes.txt) on your local system, ensuring your notes are preserved between sessions.
 - Scrollable Interface: The app includes a scrollbar for navigating through extensive notes effortlessly.

   
## Requirements

### Python

Python is required to run this application. If you don't have Python installed, follow these steps to install it:

1. **Download Python**:
   - Visit the [official Python website](https://www.python.org/downloads/) to download the latest version of Python (Python 3.x).

2. **Install Python**:
   - Follow the installation instructions for your operating system.

3. **Verify Installation**:
   - Open a terminal or command prompt.
   - Check that Python is installed by running the following command:
     
     ```bash
     python --version
     ```
   - You should see the installed Python version.
     
### Tkinter
  - Tkinter comes pre-installed with Python and does not require extra installation.

### Plyer
- To enable desktop notifications, you need to install the `plyer` library. Use the following command to install it via pip:

```bash
pip install plyer
```
 

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anarshtein/python-sticky-note.git

2. **Navigate to the project directory**:
   ```bash
   cd python-sticky-note
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

### Add a Note

- Click on the "Add Note" button and enter your note in the dialog box that appears:

### Delete a Note

- Click on the "Delete" button next to the note you wish to delete.

## Project Structure
```bash
python-sticky-note/
├── main.py
├── notes.txt
└── README.md
```
