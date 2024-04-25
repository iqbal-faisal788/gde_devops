FROM python:3.7
WORKDIR /stock_app 
COPY . /stock_app
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]