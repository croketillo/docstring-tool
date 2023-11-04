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
