import torch
import csv
import pandas as pd
import time
import streamlit as st


if torch.cuda.is_available():
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

import getLink
import getContent
import translate
import getSimilar
import getSum
import toVN

temp = getSimilar.getNameFile()

def check_file_content(file_name):
    try:
        with open(file_name, 'r',encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return False

def process_text(text):
    sentences = text.split('. ')
    result = '. '.join(sentences)
    if not result.endswith('.'):
        result = result[:result.rfind('.')]
    return result

st.title("Tin tức trong tuần")



if st.button('Thời sự'):
    if check_file_content("summary.csv") == True:
        print()
    else:
        summaries = getSum.generate_summaries(temp)
        df = pd.DataFrame(summaries)
        df.to_csv('summary.csv', index=False)

    translated_texts = []

    df = pd.read_csv('summary.csv')

    count = 0

    with open('sumary_vn.csv', 'w', encoding='utf-8') as f:
        
        for summary in df['summary']:
            try:
                if count % 2 == 0:
                    translated = toVN.gemini_api(summary, "AIzaSyDwdDVCXHms_Us52qAeHN-C-EBWpHevnjw")
                elif count % 3 == 0:
                    translated = toVN.gemini_api(summary, "AIzaSyAxQ120-5y74hULGbmxw4ZEAkmS8l-tmzM")
                else:
                    translated = toVN.gemini_api(summary, "AIzaSyBV753dJdxKKTkBYE4eW1lvUiUQSyqMVNE")
                processed = process_text(translated)
                translated_texts.append(processed)
                st.write(processed)
                f.write(processed + '\n')

            except Exception as e:
                st.write(f" ")
            finally:
                count += 1
if st.button('Thể thao'):
    if check_file_content("thethao_summary.csv") == True:
        print()
    else:
        summaries = getSum.generate_summaries(temp)
        df = pd.DataFrame(summaries)
        df.to_csv('thethao_summary.csv', index=False)

    translated_texts = []

    df = pd.read_csv('thethao_summary.csv')

    count = 0

    with open('thethao_sumary_vn.csv', 'w', encoding='utf-8') as f:
        
        for summary in df['summary']:
            try:
                if count % 2 == 0:
                    translated = toVN.gemini_api(summary, "AIzaSyDwdDVCXHms_Us52qAeHN-C-EBWpHevnjw")
                elif count % 3 == 0:
                    translated = toVN.gemini_api(summary, "AIzaSyAxQ120-5y74hULGbmxw4ZEAkmS8l-tmzM")
                else:
                    translated = toVN.gemini_api(summary, "AIzaSyBV753dJdxKKTkBYE4eW1lvUiUQSyqMVNE")
                processed = process_text(translated)
                translated_texts.append(processed)
                st.write(processed)
                f.write(processed + '\n')

            except Exception as e:
                st.write(f" ")
            finally:
                count += 1



