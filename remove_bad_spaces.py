#!/usr/bin/env python
"""A script to remove spaces before new lines in files as pep8 warns"""
import sys
import os
import re

__author__ = "Diego Izidoro"


def usage(argv):
    """Checks if script call usage was correct"""
    assert argv.__class__ == list
    if len(argv) < 2:
        sys.exit('Usage: %s text_file_name' % argv[0])
    for file_path in argv[1:]:
        if not os.path.exists(file_path):
            sys.exit('ERROR: file %s was not found!' % argv[1])


def read_file(file_path):
    """reads the file
    Args:
        file_name: name of the file
    Returns: string
        string of the file
    """
    fin = open(file_path)
    string = fin.read()
    fin.close()
    return string


def overwrite_file(file_path, string):
    """overwrites the file
    Args:
        file_name: name of the file
        string: string to be written in the file
    Returns: None
    """
    fout = open(file_path, 'w')
    fout.write(string)
    fout.close()


def correct_files(files_paths):
    """removes spaces before new lines
    Args:
        files_paths: paths to the files to be corrected
    Returns: None
    """
    for file_path in files_paths:
        string = read_file(file_path)
        corrected_string = re.sub(r" +\n", "\n", string)
        overwrite_file(file_path, corrected_string)


def main(argv):
    """main"""
    usage(argv)
    files_paths = argv[1:]
    correct_files(files_paths)

if __name__ == "__main__":
    main(sys.argv)
