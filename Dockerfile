FROM python:3.8-alpine
MAINTAINER Neale Johnston neale@team-johnston.com
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY . /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["gym.py"]
