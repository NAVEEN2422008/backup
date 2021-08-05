# backup

A simple Python utility that copies all files from a source folder to a destination folder.

## Features

- Copies every file in a source directory into a destination directory
- Interactive prompts for source and destination folder names

## Tech Stack

- Python 3 (standard library: `os`, `shutil`)

## Project Structure

```
backup/
└── backfile.py   # main copy script
```

## Installation

No external dependencies.

```bash
python3 backfile.py
```

## Usage

Run the script and enter the source and destination folder names when prompted:

```bash
python3 backfile.py
Enter source folder name: a
enter des folder name: b
```

All files from `a/` are copied into `b/`.
