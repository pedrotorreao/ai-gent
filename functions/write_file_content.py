import os


def write_file_content(working_directory, file_path, content):
    full_path_parent = os.path.abspath(working_directory)
    full_path_child = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path_child.startswith(full_path_parent):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    try:
        with open(full_path_child, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Erro: {e}"
