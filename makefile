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
unit_test:
	python manage.py test
build:
	docker build -t personal-website .
run:
	docker run -p 8000:8000 --rm personal-website:latest
deploy:
	#deploy
all:
	install lint test deploy