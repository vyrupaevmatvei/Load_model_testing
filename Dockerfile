FROM python:3.10.13

RUN apt update
RUN apt-get install -y uvicorn ssh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY models models
COPY tests tests
COPY app.py app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
