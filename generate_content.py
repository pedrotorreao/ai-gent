from google.genai import types

from config import SYSTEM_PROMPT
from call_function import *


def generate_content(client, messages, verbose=False):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[AVAILABLE_FUNCTIONS], system_instruction=SYSTEM_PROMPT
        ),
    )

    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if not response.function_calls:
        return response.text

    function_responses = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
