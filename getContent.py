import Vnexpress
import vietnamnet
import csv
import getLink


output_file_name_1 = 'vnexpress.csv'
output_file_name_2 = 'vietnamnet.csv'

vnexpress = "vnexpress"
vietnamnet = "vietnamnet"

output_file_name = 'links.csv'

if(getLink.getTag() == "1002565"):
    output_file_name_1 = 'thethao_vnexpress.csv'
    output_file_name_2 = 'thethao_vietnamnet.csv'
    vnexpress = "thethao_vnexpress"
    vietnamnet = "thethao_vietnamnet"
    output_file_name = 'thethao_links.csv'


input_file_name_1 = getLink.getOutput_links()
input_file_name_2 = getLink.getOutput_links_2()

def GetOutput_file_name():
    return output_file_name

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

def process_links_to_csv(input_file_name, output_file_name,code):
    with open(input_file_name, 'r',encoding='utf-8') as file:
        links = file.readlines()

    with open(output_file_name, 'w', newline='',encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Data'])

        for link in links:
            link = link.strip() 
            if link:
                if code == "vietnamnet":
                    result = vietnamnet.extract_content(link)
                    csvwriter.writerow([result])
                else:
                    result = Vnexpress.extract_content(link)
                    csvwriter.writerow([result])


if check_file_content(output_file_name_1) == True and check_file_content(output_file_name_2) == True:
    print()
else:
    process_links_to_csv(input_file_name_1,output_file_name_1,vnexpress)
    process_links_to_csv(input_file_name_2,output_file_name_2,vietnamnet)

file1_name = output_file_name_1
file2_name = output_file_name_2

with open(file1_name, 'r',encoding='utf-8') as file1, open(file2_name, 'r',encoding='utf-8') as file2:
    file1_content = file1.read()
    file2_content = file2.read()

with open(output_file_name, 'w',encoding='utf-8') as output_file:
    output_file.write(file1_content + '\n' + file2_content)