import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from generate_content import generate_content
from call_function import *


def main():
    load_dotenv()

    verbose_mode = False
    if "--verbose" in sys.argv:
        stdin_args = sys.argv[1 : len(sys.argv) - 1]
        verbose_mode = True
    else:
        stdin_args = sys.argv[1:]

    if not stdin_args:
        print("Hello, it's your AI-gent!")
        print("\nNo prompt given. Please, enter a valid prompt.")
        print('> Usage: python main.py "your input/prompt goes here"')
        print('\tExample: python main.py "What is the capital of Brazil?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(stdin_args)

    if verbose_mode:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose_mode)

    # response = client.models.generate_content(
    #     model="gemini-2.0-flash-001",
    #     contents=messages,
    #     config=types.GenerateContentConfig(
    #         tools=[AVAILABLE_FUNCTIONS], system_instruction=SYSTEM_PROMPT
    #     ),
    # )

    # usage = response.usage_metadata
    # prompt_tokens = usage.prompt_token_count
    # response_tokens = usage.candidates_token_count

    # if response.function_calls:
    #     function_call_part = response.function_calls[0]

    #     func_call_result = call_function(function_call_part, verbose_mode)

    # if verbose_mode:
    #     print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    #     # print(f"User prompt: {{{user_prompt}}}")
    #     # print(f"Prompt tokens: {{{prompt_tokens}}}")
    #     # print(f"Response tokens: {{{response_tokens}}}")
    # else:
    #     if response.function_calls:
    #         function_call_part = response.function_calls[0]
    #         print(
    #             f"Calling function: {function_call_part.name}({function_call_part.args})"
    #         )
    #     else:
    #         print(response.text)

    # print(f'Prompt tokens: {prompt_tokens}')
    # print(f'Response tokens: {response_tokens}')


if __name__ == "__main__":
    main()
