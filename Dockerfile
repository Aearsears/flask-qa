FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pyppeteer-install 

COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]