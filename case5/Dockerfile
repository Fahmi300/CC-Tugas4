FROM alpine:latest

RUN apk update && apk add --no-cache \
    nodejs npm \
    python3 py3-pip py3-setuptools \
    gcc g++

WORKDIR /app

COPY ./webapp/frontend ./frontend
COPY ./webapp/backend ./backend

WORKDIR /app/backend
RUN python3 -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

WORKDIR /app/frontend
RUN npm install
RUN chmod +x node_modules/.bin/next

WORKDIR /app
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
