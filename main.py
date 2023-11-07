import fire
from dotenv import load_dotenv

from tasks import scrape_and_process

load_dotenv()


def run(url: str):
    result = scrape_and_process.delay(url)
    print("Task submitted, processing in background...")
    return result.id


if __name__ == "__main__":
    fire.Fire(run)
