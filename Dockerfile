FROM python:3.11-slim

WORKDIR /app
COPY Pipfile ./
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . ./app

CMD ["pipenv", "run", "python", "main.py", "https://example.com"]