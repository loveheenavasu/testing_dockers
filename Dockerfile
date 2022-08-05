FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app/

# RUN chmod 0644 /app/*

# ENTRYPOINT ["/app/hotel_management/migrate.sh"]

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]