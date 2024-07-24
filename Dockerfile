FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN ln -fs /usr/share/zoneinfo/America/SaoPaulo /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata

EXPOSE 8000

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

CMD ["sh", "-c", "/app/entrypoint.sh"]
