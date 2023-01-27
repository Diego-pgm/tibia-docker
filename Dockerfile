FROM python:3
ADD stats_char.py /
RUN pip3 install mysql-connector

CMD ["python", "./stats_char.py"]
