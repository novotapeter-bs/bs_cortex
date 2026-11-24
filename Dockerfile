FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m cortexuser && chown -R cortexuser:cortexuser /app
USER cortexuser

ENTRYPOINT ["python", "server.py"]
