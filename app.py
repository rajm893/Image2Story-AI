from dotenv import load_dotenv, find_dotenv
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain import PromptTemplate, LLMChain,OpenAI, HuggingFaceHub
import torch

import requests
import os
import streamlit as st

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# os.getenv("HUGGINGFACEHUB_API_TOKEN")
#imgtotext to create a scenario form the picture
def img2text(url):
    image_to_text= pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    text= image_to_text(url)[0]["generated_text"]
    # print(text[0]["generated_text"])
    return text


##llm to generate a short story using gpt api key
def generate_story(scenario):
    template="""
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more tha 50 words;
    
    CONTEXT: {scenario}
    STORY:
    """
    prompt= PromptTemplate(template=template, input_variables=["scenario"])
    story_llm = LLMChain(llm=OpenAI(
    model_name="gpt-3.5-turbo", temperature=0.7),prompt=prompt,verbose=True) 
    story= story_llm.predict(scenario=scenario)
    return story

# text to speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads={
    "inputs":message
    }
    response= requests.post(API_URL,headers= headers,json=payloads)
    with open('audio.flac','wb') as file:
        file.write(response.content)
    

def main():
    st.set_page_config(page_title="img 2 audio story", page_icon="ABC")
    st.header=("Turn img into auio story")
    uploaded_file=st.file_uploader("Choose an image...", type="jpg")
    
    if uploaded_file is not None:
        bytes_data= uploaded_file.getvalue()
        with open(uploaded_file.name,"wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file,caption='Uploaded Image.',
                use_column_width=True)
        scenario=img2text(uploaded_file.name)
        story=generate_story(scenario)
        text2speech(story)
        
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)
        
        st.audio("audio.flac")

if __name__ == '__main__':
    main()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




