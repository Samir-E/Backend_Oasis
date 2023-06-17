FROM python:3.11

WORKDIR /app

RUN apt-get install libpq-dev

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
