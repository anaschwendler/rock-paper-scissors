FROM python:3.11.2-alpine3.17

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 5000

COPY . /app

CMD ["flask", "--app", "game", "run", "-h", "0.0.0.0", "--debug"]