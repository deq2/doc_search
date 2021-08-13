FROM python:3
ARG root_dir
ENV root_dir_env=${root_dir}
ADD app/ /app
ADD test/ /test
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update
RUN pip install -r requirements.txt
CMD python app.py "$root_dir_env"
