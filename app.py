import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

openai_api_key = os.environ.get("OPENAI_API_KEY")

# App Framework
st.title('GPT Based YouTube Script Generator')
prompt = st.text_input('Input your prompt here')

# Prompt Templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='Write me a YouTube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables=['title', 'wikipedia_research'],
    template='Write me a YouTube video script based on this TITLE: {title} while leveraging this '
             'wikipedia research: {wikipedia_research}'
)

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# LLMs
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show the results if a prompt is available
if prompt:
    title = title_chain.run(topic=prompt)
    wikipedia_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wikipedia_research)

    st.write(title)
    st.write(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wikipedia_research)
