# DocString Tool

DOCSTRING TOOL is a software to include/remove docstrings at the beginning of any python file found in the specified folder.

## Usage

**usage: main.py [-h] {add,del,show} ...

Tool for managing docstrings in .py files

positional arguments:
  {add,del,show}  Available subcommands
    add           Add docstrings to .py files [-r for recursive]
    del           Remove docstrings from .py files [-r for recursive]
    show          Preview docstring text

options:
  -h, --help      show this help message and exit**



### Usage add/del

**usage: main.py add [-h] [-r] directory text_file

positional arguments:
  directory        Path to the directory where the .py files are located
  text_file        Path to the external file with the text for the docstring

options:
  -h, --help       show this help message and exit
  -r, --recursive  Recursive search for .py files**

### Usage show

**usage: main.py show [-h] text_file

positional arguments:
  text_file   Path to the external file with the text for the docstring

options:
  -h, --help  show this help message and exit**


## EXAMPLE


``` python3 dstr.py add -r ./test_directory docstring_sample.txt  ```

