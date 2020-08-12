FROM python:3.8
MAINTAINER Birol AYDIN  (   1170606002@nku.edu.tr    )

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY /app .

CMD ["python","app.py"]





