FROM python:3.10


COPY urlService/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./urlModule /urlModule
WORKDIR /urlModule
RUN pip install .

COPY  urlService/urlAPI /app/urlAPI
COPY urlService/urlService /app/urlService
COPY urlService/manage.py /app/manage.py
COPY urlService/uwsgi.ini /app/uwsgi.ini
COPY urlService/tests /app/tests
WORKDIR /app

RUN python manage.py migrate
ENTRYPOINT [ "uwsgi", "uwsgi.ini" ]