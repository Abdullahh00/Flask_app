install:
	pip install -r requirements.txt

run:
	flask run

build:
	docker build -t abdullah4444/my-flask-app:1.0 .

run:
	docker run -p 5000:5000 abdullah4444/my-flask-app:1.0
	
push:
	docker push abdullah4444/my-flask-app:1.0
