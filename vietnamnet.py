import requests
from bs4 import BeautifulSoup
import bs4_utils

def extract_content(url):

        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")

        title_tag = soup.find("h1", class_="content-detail-title")
        desc_tag = soup.find("h2", class_=["content-detail-sapo", "sm-sapo-mb-0"])
        main_content_tag = soup.find("div", class_=["maincontent", "main-content"])

        if [var for var in (title_tag, desc_tag, main_content_tag) if var is None]:
            return ""

        title = title_tag.text
        description = " ".join(bs4_utils.get_text_from_tag(p) for p in desc_tag.contents)

        paragraphs = " ".join(bs4_utils.get_text_from_tag(p) for p in main_content_tag.find_all("p"))

        concatenated_text = f"{title}\n{description}\n{paragraphs}"
        return concatenated_text