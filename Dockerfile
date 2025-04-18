FROM python:3.10.5

EXPOSE 8000
WORKDIR /reproducing_churches

ADD requirements.txt /reproducing_churches/

RUN pip install -r requirements.txt

ADD ./platform /reproducing_churches

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--reload", "reproducing_churches.wsgi:application"]