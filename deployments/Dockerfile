FROM python:3
ARG root_dir
ENV root_dir_env=${root_dir}
ARG basename
ENV basename_env=${basename}
ADD app/ /app
ADD test/ /test
ADD ${basename_env} /${basename_env}
WORKDIR /${basename_env}
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update
RUN pip install -r /app/requirements.txt
CMD python /app/app.py /${basename_env}
