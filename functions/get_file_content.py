import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_path_parent = os.path.abspath(working_directory)
    full_path_child = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path_child.startswith(full_path_parent):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path_child):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path_child, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if os.path.getsize(full_path_child) > MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )

            return file_content_string

    except Exception as e:
        return f"Erro: {e}"
