FROM python:3.7-slim
RUN apt-get update && apt-get install curl -y && curl https://artifacts.eng.appianci.net/artifactory/get-vault-token/get-vault-token-linux-amd64 -o get-vault-token && chmod +x get-vault-token && mv get-vault-token /usr/local/bin
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD FLASK_APP=server.py flask run -p 7002