FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD FLASK_APP=server.py flask run -p 7002