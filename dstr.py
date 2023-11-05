""" 
This file is (or part of) DOCSTRING TOOL v1.0
Copyright 2023- Croketillo <croketillo@gmail.com> https://github.com/croketillo
 
DESCIPTION:
DOCSTRING TOOL is a software to include/remove docstrings at the beginning of-
any python file found in the specified folder.

                        LICENSE -   GNU GPL-3

This software is protected by the GNU General Public License version 3 (GNU GPL-3).
You are free to use, modify, and redistribute this software in accordance with the 
terms of the GNU GPL-3. You can find a copy of the license at the following link: 
https://www.gnu.org/licenses/gpl-3.0.html.

This software is provided as-is, without any warranties, whether express or implied. 
Under no circumstances shall the authors or copyright holders be liable for any claims, 
damages, or liabilities arising in connection with the use of this software.
If you make modifications to this software and redistribute it, you must comply with 
the terms of the GNU GPL-3, which includes the obligation to provide the source code 
for your modifications. Additionally, any derived software must also be under the 
GNU GPL-3.

For more information about the GNU GPL-3 and its terms, please carefully read the full
license or visit https://www.gnu.org/licenses/gpl-3.0.html
"""

import argparse
from docstring_tool.includedstr import *
from docstring_tool.deldstr import remove_docstrings

def main():
    print("DOCSTRING TOOL version 1.0")
    print("by Croketillo")
    print("---------------------------\n")
    parser = argparse.ArgumentParser(description='Tool for managing docstrings in .py files')
    subparsers = parser.add_subparsers(dest='subcommand', help='Available subcommands')

    # Subcommand to add docstrings
    add_parser = subparsers.add_parser('add', help='Add docstrings to .py files [-r for recursive]')
    add_parser.add_argument('directory', help='Path to the directory where the .py files are located')
    add_parser.add_argument('text_file', help='Path to the external file with the text for the docstring')
    add_parser.add_argument('-r', '--recursive', action='store_true', help='Recursive search for .py files')

    # Subcommand to remove docstrings
    remove_parser = subparsers.add_parser('del', help='Remove docstrings from .py files [-r for recursive]')
    remove_parser.add_argument('directory', help='Path to the directory where the .py files are located')
    remove_parser.add_argument('-r', '--recursive', action='store_true', help='Recursive search for .py files')

    # Subcommand to preview docstring
    preview_parser = subparsers.add_parser('show', help='Preview docstring text')
    preview_parser.add_argument('text_file', help='Path to the external file with the text for the docstring')

    args = parser.parse_args()

    if args.subcommand == 'add':
        add_docstring_to_files(args.directory, args.text_file, args.recursive)
    elif args.subcommand == 'del':
        remove_docstrings(args.directory, args.recursive)
    elif args.subcommand == 'show':
        show_docstring_preview(args.text_file)

if __name__ == '__main__':
    main()
