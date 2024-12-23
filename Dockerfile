FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build -t django .
# docker run -p 8000:8000 django
# 127.0.0.1:8000