from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import csv
import toEN
import getContent

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

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

# tokenizer = AutoTokenizer.from_pretrained("VietAI/envit5-translation")
# model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/envit5-translation").to(device)

# def summarize(text):
#     # Tóm tắt văn bản
#     inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True).to(device)
#     summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

def remove_prefix(translation):
    prefix = "en:"
    if translation.startswith(prefix):
        return translation[len(prefix):].strip()
    return translation


def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        count = 0

        for row in reader:
            try:
                original_text = row['Data']
            
                if count % 2 == 0:
                    translated_text = toEN.gemini_api(original_text, "AIzaSyDwdDVCXHms_Us52qAeHN-C-EBWpHevnjw")
                elif count % 3 == 0:
                    translated_text = toEN.gemini_api(original_text, "AIzaSyAxQ120-5y74hULGbmxw4ZEAkmS8l-tmzM")
                else:
                    translated_text = toEN.gemini_api(original_text, "AIzaSyBV753dJdxKKTkBYE4eW1lvUiUQSyqMVNE")
                
                cleaned_text = remove_prefix(translated_text)
                row['Data'] = cleaned_text
                
                writer.writerow(row)

            except Exception as e:
                print(" ")

            finally:
                count += 1

input_file_name = getContent.GetOutput_file_name()
output_file_name = 'Data_Trans.csv'

if(getContent.getLink.getTag() == "1002565"):
    output_file_name = 'Thethao_Data_Trans.csv'

if check_file_content(output_file_name) == True:
    print()
else:
    process_csv(input_file_name, output_file_name)

def getOuput():
    return output_file_name