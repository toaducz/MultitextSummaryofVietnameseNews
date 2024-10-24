import datetime

# Lấy ngày hiện tại
today = datetime.datetime.now()

# Tạo đối tượng datetime cho Unix Epoch (1/1/1970)
epoch = datetime.datetime(1970, 1, 1)

# Tính số giây từ Unix Epoch đến ngày hiện tại
unix_timestamp_today = int((today - epoch).total_seconds())

# Tính ngày trước đó 1 ngày
seven_day_ago = today - datetime.timedelta(days=7)

# Tính số giây từ Unix Epoch đến ngày trước đó 1 ngày
unix_timestamp_seven_day_ago = int((seven_day_ago - epoch).total_seconds())

#VNEXPRESS lấy theo tag

import requests
from bs4 import BeautifulSoup
import datetime

exist = []



tag =  "1002565"
cate = "&cate=000009"

output_links = "output_links.txt"
output_links_2 = "output_links_2.txt"

if(tag == "1001005"):
  output_links = "output_links.txt"
  output_links_2 = "output_links_2.txt"
  cate = "&cate=000002"
  

if(tag == "1002565"):
  output_links = "thethao_output_links.txt"
  output_links_2 = "thethao_output_links_2.txt" 
  cate = "&cate=000009"


def getTag():
  return tag;

def getOutput_links():
  return output_links

def getOutput_links_2():
  return output_links_2 
# thể thao 1002565

# thời sự 1001005

# pháp luật 1001007

# sức khỏe 1003750

root = "https://vnexpress.net/category/day/cateid/" + tag + "/fromdate/" + str(unix_timestamp_seven_day_ago)+ "/todate/"+ str(unix_timestamp_today) +"/allcate/" + tag + "/page/"


n =1

with open(output_links, 'w', encoding='utf-8') as file:
    for i in range(n, 10):
        url = root + str(i)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = soup.select('h3 a[href]')

            for article in articles:
                article_url = article['href']
                if "https://vnexpress.net" not in article_url:
                  if "ngoisao" not in article_url:

                    article_url =  "https://vnexpress.net" +  article_url
                # print(article_url)

                if "video" not in article_url and article_url not in exist:
                  exist.append(article_url)
                  file.write(article_url + '\n')
        else:
            print(f"Failed to fetch page {url}. Status code: {response.status_code}")



today = datetime.datetime.now()
formatted_date = today.strftime("%d/%m/%Y")

one_day_ago = today - datetime.timedelta(days=7)
formatted_one_day_ago = one_day_ago.strftime("%d/%m/%Y")

#cate=000002 thời sự
#cate=000009 thể thao
#cate=00000W sức khỏe
#cate=000008 pháp luật

root = "https://vietnamnet.vn/tin-tuc-24h-p"

n =0

exist = []


with open(output_links_2, 'w', encoding='utf-8') as file:
    for i in range(n, 20):
        url = root + str(i) + "?bydate=" + formatted_one_day_ago + "-" + formatted_date + cate
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = soup.select('div.horizontalPost.sm\:lineSeparates.mb-20.version-news')

            # articles = soup.select('h3 a[href]')

            for article in articles:
              main_cate = article.select_one('div.horizontalPost__main-cate.show a[href="/thoi-su"]')
              if (cate == "&cate=000009"):
                main_cate = article.select_one('div.horizontalPost__main-cate.show a[href="/the-thao"]')
              if main_cate:
                  article_url = article.select_one('h3 a[href]')['href']
                  if "https://vietnamnet.vn" not in article_url:
                    article_url =  "https://vietnamnet.vn" +  article_url

                  if "video" not in article_url and article_url not in exist:
                    exist.append(article_url)
                    file.write(article_url + '\n')
        else:
            print(f"Failed to fetch page {url}. Status code: {response.status_code}")
            
