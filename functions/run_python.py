import os
import subprocess
import sys


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
