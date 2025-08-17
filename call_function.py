from google.genai import types

from config import WORKING_DIRECTORY

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file_content import schema_write_file, write_file_content
from functions.run_python import schema_run_python_file, run_python_file

AVAILABLE_FUNCTIONS = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

FUNCTION_MAP = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file_content": write_file_content,
    "run_python_file": run_python_file,
}


def call_function(function_call_part, verbose=False):
    if verbose:
        print(
            f" - Calling function: {function_call_part.name}({function_call_part.args})"
        )
    else:
        print(f" - Calling function: {function_call_part.name}")

    func_name = function_call_part.name

    if func_name not in FUNCTION_MAP:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )

    func_args = dict(function_call_part.args)
    func_args["working_directory"] = WORKING_DIRECTORY

    func_call_result = FUNCTION_MAP[func_name](**func_args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"result": func_call_result},
            )
        ],
    )
