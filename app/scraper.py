import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, HttpUrl, ValidationError
from tenacity import retry, stop_after_attempt, wait_fixed

class ScrapedData(BaseModel):
    title: str
    url: HttpUrl

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_data(url: str) -> ScrapedData:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').get_text()
    return ScrapedData(title=title, url=url)

def process_data(data: ScrapedData):
    if "Python" in data.title:
        print(f"Python was found in the title: {data.title}")
    else:
        print("Python was not found in the title.")
