install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt
format:
	#black *.py
lint:
	#pylint --disable=R,C *.py
test:
	python manage.py runserver
build:
	docker build -t personal-website .
run:
	docker run -p 8000:8000 --rm personal-website:latest
deploy:
	#deploy
all:
	instal	l lint test deploy