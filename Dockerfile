FROM python:alpine

LABEL maintainer="Ignacio Rustan"

RUN pip install flask
COPY urlstat01.py /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/urlstat01.py"]
