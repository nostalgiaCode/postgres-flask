FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py