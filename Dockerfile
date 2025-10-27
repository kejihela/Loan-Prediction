FROM python:3.9-slim-buster

    
RUN pip install --upgrade pip

COPY . /code

RUN chmod +x /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8005

WORKDIR /code/

ENV PYTHONPATH "${PYTHONPATH}:/code/"

CMD pip install -e .