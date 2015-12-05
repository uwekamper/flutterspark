FROM ubuntu

RUN apt-get update; \
    apt-get install -y \
      python python-pip \
      python-numpy python-scipy \
      build-essential python-dev python-setuptools \
      libatlas-dev libatlas3gf-base

RUN update-alternatives --set libblas.so.3 \
      /usr/lib/atlas-base/atlas/libblas.so.3; \
    update-alternatives --set liblapack.so.3 \
      /usr/lib/atlas-base/atlas/liblapack.so.3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN (cd /code/flutterbrain_web/ && python manage.py migrate --noinput)
# RUN (cd /code/flutterbrain_web/ && python manage.py collectstatic --noinput)
EXPOSE 8000
CMD python /code/flutterbrain_web/manage.py runserver 0.0.0.0:8000
