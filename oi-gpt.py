#!/usr/bin/python3

import openai
import sys

if sys.platform == "win32":
    import win32clipboard
    def to_clipboard(text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
elif sys.platform == "darwin":
    import subprocess
    def to_clipboard(text):
        process = subprocess.Popen(
            "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
        )
        process.communicate(text.encode("utf-8"))
elif sys.platform.startswith("linux"):
    import subprocess
    def to_clipboard(text):
        process = subprocess.Popen(
            "xsel --clipboard --input", shell=True, stdin=subprocess.PIPE
        )
        process.communicate(text.encode("utf-8"))
else:
    raise Exception("Unsupported platform")

openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    if sys.argv[1] == "-h":
        print("Usage: python script.py [-c | phrase]")
        print("-c: start an infinite loop to ask questions and receive answers")
        print("phrase: the phrase to ask CHATGPT (enclosed in quotes if it contains spaces)")
    elif sys.argv[1] != "-c":
        prompt = sys.argv[1]
        response = generate_response(prompt)
        print(response)
        to_clipboard(response)
    else:
        while True:
            prompt = input("Enter a question (or 'exit' to exit): ")
            if prompt.strip().lower() == "exit":
                break
            response = generate_response(prompt)
            print(response)
            to_clipboard(response)

