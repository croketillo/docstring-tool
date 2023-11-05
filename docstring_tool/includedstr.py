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
import sys

def add_docstring_to_files(directory, text_file, recursive, config_file="docstring.cnf"):
    try:
        # Read the content of the configuration file
        with open(config_file, 'r') as f:
            config_text = f.read()

        # Search for tags and values in the configuration file
        tags = dict(re.findall(r'\[(\w+)\]=([^[\n]+)', config_text))

        # Read the content of the text file
        with open(text_file, 'r') as f:
            docstring_text = f.read()

        # Replace tags in the content of the text file
        for tag, value in tags.items():
            tag_format = f"[{tag}]"
            formatted_value = format_tag(value)
            docstring_text = docstring_text.replace(tag_format, formatted_value)

    except FileNotFoundError:
        response = input("'docstring.cnf' not found. Do you want to continue? (Y/N): ").strip().lower()
        if response == "y":
            with open(text_file, 'r') as f:
                docstring_text = f.read()
        else:
            print("No changes have been made to the files.")
            sys.exit(0)

    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    py_file = os.path.join(root, file)

                    with open(py_file, 'r') as f:
                        py_content = f.read()

                    # Check if the .py file already has a docstring at the beginning
                    if py_content.strip().startswith('"""'):
                        print(f'The file already has a docstring, skipping: {py_file}')
                        continue

                    try:
                        # Open the .py file in write mode and add the docstring at the beginning
                        with open(py_file, 'w') as f:
                            f.write(f'"""{docstring_text}"""\n\n')
                            f.write(py_content)
                    except Exception as e:
                        print(f"Error writing to the .py file: {py_file}\nError: {str(e)}")
                        continue

                    print(f'Docstring added to the file: {py_file}')
    else:
        for file in os.listdir(directory):
            if file.endswith('.py'):
                py_file = os.path.join(directory, file)

                with open(py_file, 'r') as f:
                    py_content = f.read()

                # Check if the .py file already has a docstring at the beginning
                if py_content.strip().startswith('"""'):
                    print(f'The file already has a docstring, skipping: {py_file}')
                    continue

                try:
                    # Open the .py file in write mode and add the docstring at the beginning
                    with open(py_file, 'w') as f:
                        f.write(f'"""{docstring_text}"""\n\n')
                        f.write(py_content)
                except Exception as e:
                    print(f"Error writing to the .py file: {py_file}\nError: {str(e)}")
                    continue

                print(f'Docstring added to the file: {py_file}')

def format_tag(tag):
    formatted_tag = ""
    words = tag.split()
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= 80:
            current_line += " " + word
        else:
            formatted_tag += current_line + "-\n"
            current_line = word

    formatted_tag += current_line

    return formatted_tag

def show_docstring_preview(text_file, config_file="docstring.cnf"):
    try:
        with open(config_file, 'r') as f:
            config_text = f.read()

        # Search for tags and values in the configuration file
        tags = dict(re.findall(r'\[(\w+)\]=([^[\n]+)', config_text))

        with open(text_file, 'r') as f:
            docstring_text = f.read()

        # Apply format_tag to tag values
        for tag, value in tags.items():
            formatted_value = format_tag(value)
            tags[tag] = formatted_value

        # Replace tags in the content of the text file
        for tag, value in tags.items():
            tag_format = f"[{tag}]"
            docstring_text = docstring_text.replace(tag_format, value)

        print(f'"""{docstring_text}"""\n')
    except FileNotFoundError:
        print("File not found: ", text_file)

