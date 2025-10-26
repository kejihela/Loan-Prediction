FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    RUN pip install --upgrade pip

COPY . /code

RUN chmod +x /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8005

WORKDIR /code/

ENV PYTHONPATH "${PYTHONPATH}:/code/"

CMD pip install -e .