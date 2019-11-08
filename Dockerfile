FROM python:3.6

RUN apt-get update

RUN mkdir /code

COPY . /code/

WORKDIR /code

#COPY config/local.py.example config/local.py

RUN pip install -r requirements.txt

# variables
ARG BUILD="dev"
ARG DEBUG="False"
ARG AWS_DEFAULT_REGION="us-east-2"
ARG JWT_SECRET_KEY=""

# variables
ENV BUILD=${BUILD}
ENV DEBUG=${DEBUG}
ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
ENV JWT_SECRET_KEY=${JWT_SECRET_KEY}

#RUN python manage.py collectstatic --noinput

#RUN python manage.py migrate

EXPOSE 8005

CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
