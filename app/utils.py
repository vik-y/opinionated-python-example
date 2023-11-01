from celery import Celery
from .scraper import fetch_data, process_data
app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def scrape_and_process(url: str):
    try:
        data = fetch_data(url)
        process_data(data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")