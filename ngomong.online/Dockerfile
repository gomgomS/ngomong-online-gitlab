FROM python:slim
WORKDIR /ngomong_online
COPY . /ngomong_online

RUN pip install -r requirements.txt

ENV FLASK_APP=server.py 
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

CMD ["flask","run","--host=0.0.0.0", "--port=5000"]
