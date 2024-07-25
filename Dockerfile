FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY .env /app/.env
COPY brain_agriculture /app/brain_agriculture
COPY requirements.txt /app/requirements.txt
COPY manage.py /app/manage.py

RUN ln -fs /usr/share/zoneinfo/America/SaoPaulo /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata

EXPOSE 8000

RUN pip install -r requirements.txt

RUN gunicorn brain_agriculture.wsgi:application --name brain_agriculture --workers 3 --user=root --bind=0.0.0.0:$PORT --log-level=debug --log-file=-

