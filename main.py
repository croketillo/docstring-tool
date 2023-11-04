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
