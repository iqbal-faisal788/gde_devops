The tool is used to provide the closing price of a NASDAQ stock by the ticker symbol. It is built using Python Flask.

To run locally : python3 app.py 

To run containerized:

build image using docker build . -t webapp:1.0.0
run the container with docker run -d -p 8080:8080 webapp:1.0.0
application will listen on port 8080, you can access it on http://localhost:8080
