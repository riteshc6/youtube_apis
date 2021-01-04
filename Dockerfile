FROM python:3.8-buster

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /youtube_apis
WORKDIR /youtube_apis
ENV MODULE_NAME youtube_apis

ENV PYTHONPATH="${PYTHONPATH}:/youtube_apis/app"
EXPOSE 8000
EXPOSE 9200
EXPOSE 9300
CMD ["gunicorn", "app.main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
