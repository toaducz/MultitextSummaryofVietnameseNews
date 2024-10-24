import pandas as pd
from nltk.translate.bleu_score import corpus_bleu
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM
import os
import torch
import getLink


if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


config2 = PeftConfig.from_pretrained("toanduc/long-t5-tglobal-base-lora-finetuned")
base_model2 = AutoModelForSeq2SeqLM.from_pretrained("google/long-t5-tglobal-base")
model2 = PeftModel.from_pretrained(base_model2, "toanduc/long-t5-tglobal-base-lora-finetuned").to(device)
tokenizer2 = AutoTokenizer.from_pretrained("google/long-t5-tglobal-base")

tag = getLink.getTag()

keyword = 'group'

if(tag == "1002565"):
    keyword = 'thethao_group'

model2 = model2.merge_and_unload()

def generate_summaries(text_files):
    summaries = []

    for file_path in text_files:
        if keyword in os.path.basename(file_path):
            
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            
            input_text = text
            inputs = tokenizer2.encode(input_text, return_tensors="pt", max_length=4096, truncation=True).to(device)

            
            outputs = model2.generate(inputs, max_length=512, length_penalty=1.0, num_beams=5, early_stopping=True)
            summary = tokenizer2.decode(outputs[0], skip_special_tokens=True)

            summaries.append({
                'file': os.path.basename(file_path),
                'summary': summary
            })
            print(f"Completed summarizing {file_path}")

    return summaries