FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "exceptions1", "worker", "--loglevel=INFO", "-n", "exceptions1", "-Q", "exceptions1Q"]