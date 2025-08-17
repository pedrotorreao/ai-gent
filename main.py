import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from generate_content import generate_content
from call_function import *
from config import MAX_ITERS


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

    iteration_count = 0
    while True:
        iteration_count += 1
        if iteration_count > MAX_ITERS:
            print(
                f"You fave reached your iteration limit ({MAX_ITERS}). Add credits if you wish to continue."
            )
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose_mode)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

    # generate_content(client, messages, verbose_mode)


if __name__ == "__main__":
    main()
