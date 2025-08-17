import os
import subprocess


from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=[]):
    full_path_directory = os.path.abspath(working_directory)
    full_script_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_script_path.startswith(full_path_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_script_path):
        return f'Error: File "{file_path}" not found.'

    if not full_script_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command_args = ["python", full_script_path]
        if len(args) > 0:
            command_args += args

        result = subprocess.run(
            command_args,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )

        response = []

        if result.stdout:
            response.append(f"STDOUT:{result.stdout}")

        if result.stderr:
            response.append(f"STDERR:{result.stderr}")

        if result.returncode != 0:
            response.append(f"Process exited with code {result.returncode}")

        return "\n".join(response) if response else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
