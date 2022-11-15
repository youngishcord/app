FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "exceptions2", "worker", "--loglevel=INFO", "-n", "exceptions2", "-Q", "exceptions2Q"]