import requests
from bs4 import BeautifulSoup

def extract_content(url):
        """
        Extract title, description, and paragraphs from url and concatenate them into a single string.
        @param url (str): url to crawl
        @return concatenated_text (str): Text containing title, description, and paragraphs
        """
        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")

        title_tag = soup.find("h1", class_="title-detail") 
        if title_tag is None:
            return ""

        title = title_tag.text.strip()

        description_tag = soup.find("p", class_="description")
        description = description_tag.text.strip() if description_tag else ""

        paragraph_tags = soup.find_all("p", class_="Normal")
        paragraphs = "\n".join(p.text.strip() for p in paragraph_tags)

        concatenated_text = f"{title}\n{description}\n{paragraphs}"

        return concatenated_text