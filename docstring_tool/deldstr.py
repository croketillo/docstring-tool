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

import os
import re

def remove_docstrings(directory, recursive):
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    py_file = os.path.join(root, file)
                    remove_docstring_from_file(py_file)
    else:
        for file in os.listdir(directory):
            if file.endswith('.py'):
                py_file = os.path.join(directory, file)
                remove_docstring_from_file(py_file)

def remove_docstring_from_file(py_file):
    try:
        with open(py_file, 'r') as f:
            py_content = f.read()

        # Use a regular expression to remove the docstring (including initial quotes)
        content_without_docstring = re.sub(r'(["\']{3}.*?["\']{3})', '', py_content, flags=re.DOTALL)

        # Remove leading blank lines from the file
        content_without_docstring = content_without_docstring.lstrip('\n')

        with open(py_file, 'w') as f:
            f.write(content_without_docstring)

        print(f'Docstring removed from file: {py_file}')
    except Exception as e:
        print(f"Error processing .py file: {py_file}\nError: {str(e)}")
