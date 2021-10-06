FROM python:3.8.2-alpine

WORKDIR /USFA_WEBSITE

ADD . /USFA_WEBSITE

RUN pip install -r requirements.txt

CMD ["python","application.py"]

#docker image build -t usfa_website .

#docker ps -a

# docker run -p 5000:5000 -d usfa_website
#docker stop [ID]