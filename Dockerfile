FROM python:3.8
MAINTAINER Soboliev Yuriy
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /newsaggregator
WORKDIR /newsaggregator
ENV FLASK_ENV=development
COPY . /newsaggregator
RUN pip install -r requirements.txt
COPY wait-db.sh /bin/wait-db.sh
RUN chmod +x /bin/wait-db.sh
CMD ["python", "app.py"]
