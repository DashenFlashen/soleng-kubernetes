FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

COPY ./app.py /app

CMD ["python", "app.py"]
