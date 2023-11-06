# DocString Tool

DOCSTRING TOOL is a software to include/remove docstrings at the beginning of any python file found in the specified folder.
The docstring text is stored in a file that will be specified by the user. It is possible to store tags to include in the text in ```docstring.cnf``` to be able to reuse docstring texts.


## Usage

```usage: dstr.py [-h] {add,del,show} ...

Tool for managing docstrings in .py files

positional arguments:
  {add,del,show}  Available subcommands
    add           Add docstrings to .py files [-r for recursive]
    del           Remove docstrings from .py files [-r for recursive]
    show          Preview docstring text

options:
  -h, --help      show this help message and exit```



### Usage add/del

Adds or removes the docstring specified in the file to all files with the extension ".py" in the specified directory.

```usage: dstr.py add [-h] [-r] directory text_file

positional arguments:
  directory        Path to the directory where the .py files are located
  text_file        Path to the external file with the text for the docstring

options:
  -h, --help       show this help message and exit
  -r, --recursive  Recursive search for .py files```

### Usage show

Shows how the docstring of the specified file looks like.

```usage: dstr.py show [-h] text_file

positional arguments:
  text_file   Path to the external file with the text for the docstring

options:
  -h, --help  show this help message and exit```


## EXAMPLE


``` python3 dstr.py add -r ./test_directory docstring_sample.txt  ```

