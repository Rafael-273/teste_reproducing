FROM python:3.10.5

EXPOSE 8000
WORKDIR /ever_desk

ADD requirements.txt /ever_desk

RUN pip install -r requirements.txt

ADD ./ever_desk /everdesk

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--reload", "everdesk.wsgi:application"]