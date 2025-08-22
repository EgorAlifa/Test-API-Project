FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
