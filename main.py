import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    
    verbose_mode = False
    if '--verbose' in sys.argv:
        stdin_args = sys.argv[1:len(sys.argv)-1]
        verbose_mode = True
    else:
        stdin_args = sys.argv[1:] 

    if not stdin_args:
        print("No prompt given. Please, enter a valid prompt.")
        print('Usage: python main.py "your input/prompt goes here"')
        print('- Example: python main.py "What is the capital of Brazil?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(stdin_args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages)
    
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count
    
    if verbose_mode:
        print(f'User prompt: {{{user_prompt}}}')
        print(f'Prompt tokens: {{{prompt_tokens}}}')
        print(f'Response tokens: {{{response_tokens}}}')
    else:
        print(response.text)
    # print(f'Prompt tokens: {prompt_tokens}')
    # print(f'Response tokens: {response_tokens}')



if __name__ == "__main__":
    main()
