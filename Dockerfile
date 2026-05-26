FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser -D ckaduser

WORKDIR /app

COPY requirements.txt .
    RUN pip install --no-cache-dir --upgrade pip setuptools "wheel>=0.46.2" && \
        pip install --no-cache-dir "jaraco.context>=6.1.0" && \
        pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R ckaduser:ckaduser /app
USER ckaduser

EXPOSE 8080

CMD ["python", "app.py"]