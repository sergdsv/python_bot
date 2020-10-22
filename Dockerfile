FROM python:3.7

WORKDIR /usr/src/app

RUN apt-get install -y git

RUN git clone git@github.com:sergdsv/python_bot.git
RUN pip install --no-cache-dir -r requirements.txt


#COPY . .
#
#CMD [ "python", "./app.py" ]
