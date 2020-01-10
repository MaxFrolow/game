
FROM mediasapiens/python3

RUN mkdir /web
WORKDIR /web
COPY req.txt /req.txt
RUN apt-get update && apt-get -y install python3-pip libz-dev libjpeg-dev libfreetype6-dev python-dev
RUN pip install -r /req.txt && rm /req.txt