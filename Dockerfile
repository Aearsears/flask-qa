FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
ENV TRANSFORMERS_CACHE='/root/.cache/torch/transformers'
ENV HF_DATASETS_OFFLINE=1 
ENV TRANSFORMERS_OFFLINE=1

WORKDIR /app

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . .

RUN python3 -c "from library.pipelines import pipeline; pipe = pipeline(\"multitask-qa-qg\")"

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]