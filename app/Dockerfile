FROM python:3.6-alpine

EXPOSE 5000
EXPOSE 3306

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python -u app.py
