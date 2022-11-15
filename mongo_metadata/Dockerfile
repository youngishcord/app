FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "mongo_metadata", "worker", "--loglevel=INFO", "-n", "mongo_metadata", "-Q", "mongo_metadata"]