import os

from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


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
