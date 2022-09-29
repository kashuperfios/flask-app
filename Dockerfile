FROM python:alpine3.7
COPY . /app
WORKDIR /app
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONUNBUFFERED=1
# RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# RUN python3 -m ensurepip
# RUN pip3 install --no-cache --upgrade pip setuptools

# RUN apk add --update python3 py3-pip
# COPY requirements.txt app/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5005

# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]