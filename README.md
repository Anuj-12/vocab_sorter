# Obsidian Vocabulary Sorter

A Python script to automatically sort German vocabulary `.md` files exported from Obsidian into alphabetical folders.

## Features

- Handles special German characters (Ä, Ö, Ü, ß)
- Sorts files into A-C, D-F, ..., Y-Z folders

## Usage

1. Set the current working directory (cwd) and the target directory (target) in main.py
2. Run the script with Python 3.10+.

## Automation

To run this script automatically (e.g. at 2 am every morning) add the following line to your crontab :  
0 2 * * * /usr/bin/python3 *location of the srcipt*
