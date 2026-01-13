FROM python:3.12-slim

WORKDIR /app

COPY app1/app.py /app/app1.py
COPY app2/app.py /app/app2.py

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python /app/${SERVICE_NAME}.py"]
