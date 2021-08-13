FROM python:3
ADD app/ /app
ADD test/ /test
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update
RUN pip install -r requirements.txt
CMD python app.py
