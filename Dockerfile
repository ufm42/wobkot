FROM python:3.12-slim

WORKDIR /wobkot

COPY . /wobkot

EXPOSE 443

CMD ["python", "host.py"]
