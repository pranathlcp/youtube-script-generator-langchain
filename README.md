# GPT Based YouTube Script Generator

This repository contains code for a YouTube script generator based on the OpenAI API. It utilizes OpenAI's ChatGPT model to generate titles and scripts for YouTube videos. The generator takes user prompts, performs Wikipedia research, and generates engaging titles and scripts accordingly.

## Installation

To use this script generator, follow these steps:

1. Clone the repository: `git clone https://github.com/pranathlcp/youtube-script-generator-langchain.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Obtain an API key from OpenAI and set it as the `OPENAI_API_KEY` environment variable.
4. Run the script: `streamlit run app.py`

## Usage

Once the script generator is running, you will be prompted to input your desired prompt. The generator will then generate a YouTube video title and script based on the provided prompt. It leverages Wikipedia research to enhance the script generation process.

The generated title, script, and relevant history are displayed in the user interface. The title history, script history, and Wikipedia research details can be expanded for more information.

## Customization

To customize the prompt templates or adjust the behavior of the language model, you can modify the code in the respective sections. You can also experiment with different temperature values to control the randomness of the generated output.

Feel free to explore and adapt the code according to your specific requirements.