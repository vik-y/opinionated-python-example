import os

from celery import Celery

from scraper import fetch_data, process_data

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

app = Celery("tasks", broker=REDIS_URL)


@app.task
def scrape_and_process(url: str):
    try:
        data = fetch_data(url)
        process_data(data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
