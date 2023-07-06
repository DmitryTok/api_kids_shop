.PHONY: up
up: superuser
	docker-compose up

.PHONY: close_docker-compose_file
down:
	docker-compose stop

.PHONY: db
db:
	docker-compose up -d db

makemigrations: db
	docker-compose run web python manage.py makemigrations

migrate: makemigrations
	docker-compose run web python manage.py migrate

loaddata: migrate
	docker-compose run web python manage.py load_data data/goods.csv

superuser: loaddata
	docker-compose run web python manage.py createsuperuser
