FROM python:3.10-alpine

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]