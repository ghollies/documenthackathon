FROM python:3.6-slim

# Copy requirements and install dependencies
COPY ./server/requirements.txt /server/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /server/requirements.txt

# Copy application server
COPY ./server/server.py /server/server.py

ENTRYPOINT ["python", "/server/server.py"]
