import streamlit as st
from utils.utils import slowedreverb
import subprocess as sp
import os

st.set_page_config(page_title='LOFI-Converter', layout='centered')


def process():
    infile = "new"+str(file.name)
    with open(infile, 'wb') as f: #Saving file
        f.write(file.getbuffer())

    # global outfile
    outfile =  "[LOFI]"+file.name
    
    slowedreverb(infile, outfile)
    
    # st.write(file)

    sp.call(f'del "{infile}"', shell =True)

    # st.audio(outfile)



def clean():
    sp.call(f'del "{"[LOFI]"+file.name}"', shell=True)

file = st.file_uploader("Audio file")

if file is not None:
    st.audio(file)
    but = st.button('PROCESS', on_click=process)
    if but:
        st.write('DONE', "[LOFI]"+file.name)
        st.audio("[LOFI]"+file.name)
        with open("[LOFI]"+file.name, 'rb') as filee:
            st.download_button(label="Download LOFI", data=filee, file_name="[LOFI]"+file.name, on_click=clean)

