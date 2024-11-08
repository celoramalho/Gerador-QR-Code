#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode
import qrcode.image.svg
import pandas as pd
import numpy as np
import re
import unicodedata
import os
from pathlib import Path
import json
from pprint import pprint
from datetime import date, time, datetime


# In[2]:


def __get_real_path():
    realpath = os.getcwd()
    return realpath


# In[3]:


def __clean_text(text):
    # Normalize text to decompose accented characters
    nfkd_form = unicodedata.normalize('NFKD', text)
    # Remove accents by keeping only ASCII characters
    text_without_accents = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    # Remove special characters, keeping only letters, numbers, and spaces
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text_without_accents)
    # Replace spaces with underscores and convert to lowercase
    clean_text = clean_text.replace(" ", "_").lower()
    return clean_text


# In[ ]:


def __create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# In[4]:


def excel_to_df(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Check the file path and name.")


# In[5]:


def generate_qr_code_excel_file():
    qr = qrcode.QRCode(version=1)
    realpath = __get_real_path()

    excel_filepath = f"{realpath}/Planilha/Planilha_QR_Code.xlsx"
    #check if already have a line with the same serialnumber

    df = excel_to_df(excel_filepath)

    # Get the current date and time
    current_datetime = datetime.now()

    # Format it to be suitable for a folder name
    folder_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    __create_folder(folder_name)


    links_list = df['Link pro QRCode']
    for index, link in enumerate(links_list):
        qr.add_data(link)
        img = qrcode.make(link)
        filetmp = f"QRCode_{index+1}-{__clean_text(df['Nome do QRCode'][index])}.png"
        img.save(f"{realpath}/QRCodes/{folder_name}/{filetmp}")


# In[6]:


generate_qr_code_excel_file()

