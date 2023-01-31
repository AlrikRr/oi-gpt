# オイ, GPT ! 
![Oi GPT](assets/oi-gpt.png)

This Python script uses the OpenAI API to generate responses to questions using CHATGPT. It supports three different modes of operation, specified by a single command-line argument:

- `-h`: Display a help menu that explains how to use the script.
- `-c`: Start an infinite loop to ask questions and receive answers. The loop continues until the user enters `exit`.
- `phrase`: A string that represents the question to ask CHATGPT.

## Requirements

- Python 3.x
- OpenAI API key
- The `openai` library: `pip install openai`
- Clipboard library for your operating system: `win32clipboard` for Windows, `subprocess` for macOS and Linux
- Install `xsel` for Linux system

## Usage

```bash
python script.py [-c | phrase]
```
- `-c`: Start an infinite loop to ask questions and receive answers.
- `phrase`: The phrase to ask CHATGPT. Enclose the phrase in quotes if it contains spaces.

## Output

The script outputs the response from CHATGPT to the console and saves it to the system clipboard.

## Note

This script was generated using OpenAI's CHATGPT language model.
