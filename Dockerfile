FROM python:3.11-bullseye
RUN mkdir -p /usr/src/app/ecom
WORKDIR /usr/src/app/ecom
RUN python -m venv venv
COPY requirements.txt ./
RUN venv/bin/pip install --no-cache-dir -r ./requirements.txt
COPY app /usr/src/app/ecom/app
COPY *.py /usr/src/app/ecom/
COPY data.json /usr/src/app/ecom/
COPY boot.sh /usr/src/app/ecom/
COPY .env /usr/src/app/ecom/
RUN chmod +x /usr/src/app/ecom/boot.sh
ENV FLASK_APP run.py
ENTRYPOINT ["./boot.sh"]
EXPOSE 5050