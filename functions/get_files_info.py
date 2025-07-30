import os


def get_files_info(working_directory, directory="."):
    full_path_parent = os.path.abspath(working_directory)
    full_path_child = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path_child.startswith(full_path_parent):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path_parent):
        return f'Error: "{working_directory}" is not a directory'

    if not os.path.isdir(full_path_child):
        return f'Error: "{directory}" is not a directory'

    try:
        files_info = []
        for filename in os.listdir(full_path_child):
            filepath = os.path.join(full_path_child, filename)
            filesize = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)

            files_info.append(
                f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
