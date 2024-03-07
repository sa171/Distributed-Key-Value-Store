FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["huey_consumer.py","tasks.huey_queue","-w","4"]




