FROM python:3.9-alpine

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN python3 -m venv fancode_sports_venv

RUN source fancode_sports_venv/bin/activate

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 3000

CMD python3 app.py

