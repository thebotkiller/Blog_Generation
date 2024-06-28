import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers

## Function to get response from LLama model
def getllamaresponse(input_text,no_words,for_whom):
    ## LLama model is called
    llm = ctransformers.CTransformers(model='C:\Python\BlogGeneration\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type= 'llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})

    ## Prompt Template

    template = """

        Write a blog for {for_whom} job profile for a topic {input_text} within {no_words} words.

        """

    prompt = PromptTemplate(input_variables=["for_whom","input_text","no_words"], template= template)

    ## Generating response from the LLama 2 model
    response = llm(prompt.format(for_whom= for_whom, input_text=input_text, no_words = no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs", layout='centered',initial_sidebar_state='collapsed')

st.header("Generate Blog")

input_text = st.text_input("Enter a topic for the Blog: ")

## Creating 2 columns for misc. fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No. of Words:')
with col2:
    for_whom = st.selectbox('Who is this for?', options=('Researchers','Data Scientists','Common People'), index=0)

submit = st.button("Generate Output")

## Final Response

if submit:
    st.write(getllamaresponse(input_text,no_words,for_whom))