FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /test

WORKDIR /test

COPY requirements.txt /test/

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /test/

RUN chmod 777 /test/*

# CMD ["sh", "test/migrate.sh"]

RUN bash -c "/test/migrate.sh"

# ENTRYPOINT ["/test/migrate.sh"]

# CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]