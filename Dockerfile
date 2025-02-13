FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download en_core_web_sm

COPY ./main.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
