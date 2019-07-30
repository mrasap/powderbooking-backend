# source: https://hub.docker.com/_/python
FROM python:3.7.3-alpine3.9

COPY requirements.txt requirements.txt

# psycopg2 source: https://hub.docker.com/r/svlentink/psycopg2/dockerfile
# uWSGI source: https://hub.docker.com/r/infrastructureascode/uwsgi/dockerfile
RUN apk add --virtual .build-deps --no-cache linux-headers build-base postgresql-dev && \
    # install the dependencies required during runtime
    apk add --no-cache libpq && \
    # install the actual python packages
    pip3 install -r requirements.txt && \
    # cleanup the build dependencies
    apk del --purge .build-deps && \
    rm -vrf /var/cache/apk/* && \
    # check what is installed
    pip3 list

# Copy the application
COPY . /app

# Create a non-root user
RUN adduser -D dummyuser && \
    chown dummyuser /app

WORKDIR app
USER dummyuser

EXPOSE 8080

CMD ["/usr/local/bin/uwsgi", "--ini", "uwsgi.ini"]