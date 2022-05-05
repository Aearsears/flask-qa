FROM python:3.8-slim-buster

WORKDIR /app

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . .

RUN python3 -c "from lib.pipelines import pipeline; pipe = pipeline(\"multitask-qa-qg\")"

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]