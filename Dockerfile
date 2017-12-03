FROM python:2

COPY requirements.txt /usr/src

WORKDIR /usr/src

RUN pip install -r requirements.txt

COPY . /usr/src/

WORKDIR /usr/src

CMD ["python","main.py","|","tee","debug.log"]
