FROM python:3.9-alpine

WORKDIR /app/

COPY /res/. .
RUN pip install -r requirements.txt

# Default di Flask
EXPOSE 5000

#CMD ["python", "app.py"]
CMD ["flask", "run", "--host=0.0.0.0"]