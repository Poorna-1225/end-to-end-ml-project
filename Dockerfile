from python:3.8-slim-buster

run apt update -y && apt install awscli -y
workdir /app

copy . /app
run pip install -r requirements.txt

cmd ['python3','app.py']