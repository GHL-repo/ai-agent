import argparse
import os
from logging import raiseExceptions

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import available_functions, call_function
from prompts import system_prompt


def get_api_key():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No valid API key found")
    else:
        return api_key


def get_user_prompt():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def generate_content(client, args, messages):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if args.verbose:
        print("User prompt: ", args.user_prompt)
        if response.usage_metadata is not None:
            print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
            print("Response tokens: ", response.usage_metadata.candidates_token_count)
        else:
            raise RuntimeError("No usage metadata found")

    f_calls = response.function_calls

    f_results_list = []
    if f_calls is not None:
        for call in f_calls:
            function_call_result = call_function(call, args.verbose)
            if not function_call_result.parts:
                raise Exception("No function call results")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Function response is None")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Function response is None")
            f_results_list.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    print("Response: ", response.text)


def main():
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)
    args = get_user_prompt()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    generate_content(client, args, messages)


if __name__ == "__main__":
    main()
